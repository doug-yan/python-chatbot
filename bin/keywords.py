from watson_developer_cloud import AlchemyLanguageV1

def print_keywords(keywords):
	print "These are the keywords that I could find: "
	for i in range(0, len(keywords)):
		print keywords[i]['text']

#Enter Sentence - Get Keywords
def getKeywords():
	alchemy_language = AlchemyLanguageV1(api_key='956ca434660f63b29b308524571beb57ee18e180')

	user_input = raw_input("Enter a sentence that you want to analyze ('q' to quit): ")

	while user_input != 'q':
		json_response = alchemy_language.keywords(text=user_input, language='english')

		length = len(json_response["keywords"])

		if length == 0:
			print "There are no keywords. Try another sentence."

		
		else:
			print_keywords(json_response["keywords"])

			user_input = raw_input("Do you want to use another sentence? (Y/N) ")
			if user_input == 'n' or user_input == 'N':
				user_input = 'q'
				break
		user_input = raw_input("Enter a sentence that you want to analyze ('q' to quit): ")