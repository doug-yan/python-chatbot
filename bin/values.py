import unirest
from thesaurus import thesaurus as get_syn

def getValues():
	#TODO: Get suggestions working
	# suggestions = raw_input("Would you like some suggestions for your entity? (Y/N) ")
	# if suggestions == 'y' or suggestions == 'Y':
	# 	url_base = 'https://wordsapiv1.p.mashape.com/words/'
	# 	word = entity 
	# 	call_type = '/hasTypes'
	# 	url = url_base + word + call_type
	# 	response = unirest.get(url,
	# 	  headers={
	# 	    "X-Mashape-Key": "MAj5SaQJGYmsh4WS1zpILm5h3EhMp1QG1ZNjsnripE92FdtaSD",
	# 	    "Accept": "application/json"
	# 	  }
	# 	)

	# 	print "Here are some suggestions: "
	# 	print response.raw_body

	value = raw_input("Enter a value for your entity ('q' to quit): ")
	jsonString = ''

	while value != 'q':
		haveSynonym = False
		jsonString += '{"value":"'
		jsonString += value
		jsonString += '","metadata:":null,"synonyms":['

		choice = raw_input("Would you like some synonyms for your value? (Y/N) ")
		if choice == 'y' or choice == 'Y':
			synonyms = get_syn(value)
			print "Here are the synonyms for " + value + ": "
			for i in range(0, len(synonyms)):
				print synonyms[i]

		choice = raw_input("Enter some synonyms for your value ('q' to quit): ")
		while choice != 'q' and choice != 'Q':
			haveSynonym = True
			jsonString += '"' 
			jsonString += choice
			jsonString += '",'
			choice = raw_input("Enter some synonyms for your value ('q' to quit): ")

		if haveSynonym == True:
			jsonString = jsonString[:-1]
		jsonString += ']},'
		value = raw_input("Enter a value for your entity ('q' to quit): ")

	jsonString = jsonString[:-1]
	return jsonString