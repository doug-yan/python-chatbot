from thesaurus import thesaurus as get_syn

def getValues(entity, values):
	value = raw_input("Enter a value for your entity ('q' to quit): ")
	while value != 'q':
		synonyms = get_syn(value)
		print "Here are the synonyms for " + value + ": "
		for i in range(0, len(synonyms)):
			print synonyms[i]

		value = raw_input("Enter a value for your entity ('q' to quit): ")