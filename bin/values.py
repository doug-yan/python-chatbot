import unirest
from thesaurus import thesaurus as get_syn

def getValues(entity, values):
	suggestions = raw_input("Would you like some suggestions for your entity? (Y/N) ")
	#TODO: Get suggestions working
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
	while value != 'q':
		synonyms = get_syn(value)
		print "Here are the synonyms for " + value + ": "
		for i in range(0, len(synonyms)):
			print synonyms[i]

		value = raw_input("Enter a value for your entity ('q' to quit): ")