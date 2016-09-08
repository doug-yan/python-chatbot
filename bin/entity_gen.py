import entities
import json
import thesaurus
from watson_developer_cloud import AlchemyLanguageV1

def print_keywords(keywords):
	print "Here are the keywords: "
	for i in range(0, len(keywords)):
		print keywords[i]

alchemy_language = AlchemyLanguageV1(api_key='956ca434660f63b29b308524571beb57ee18e180')

def app():
	#create value and add to list 
	#for each value, find synonyms, add to list (optional, use can choose which synonyms to add to list)
	#export list of entities, values, and synonyms

	entities = []
	values = []

	#Use AlchemyAPI to get keywords so that users can get an idea for what kind of entities they should create
	get_analysis = raw_input("Would you like to use a few sentences to help you come up with entities? (Y/N) ")
	if get_analysis == 'y' or get_analysis == 'Y':
		getKeywords()

	#Users create entities and values, and then get synonyms to those values
	getEntities(entities, values)


#Enter Sentence - Get Keywords
def getKeywords():
	user_input = ''
	length = 0

	user_input = raw_input("Enter a sentence that you want to analyze ('x' to quit): ")
	while user_input != 'x':
		while length < 1:
			keywords = []

			json_response = alchemy_language.keywords(text=user_input, language='english')

			length = len(json_response["keywords"])

			if length == 0:
				print "There are no keywords. Try another sentence."
			
			else:
				for i in range(0, length):
					keywords.append(json_response["keywords"][i]["text"])
				print "These were the keywords that I could find: "
				for i in range(0, length):
					print keywords[i]
				user_input = raw_input("Do you want to use another sentence? (Y/N) ")
				if user_input == 'n' or user_input == 'N':
					user_input = 'x'
					break
				length = 0

def getEntities(entities, values):
	continue_entities = raw_input("Enter an entity name ('x' to quit): ")
	while continue_entities != 'x':
		entities.append(continue_entities)
		getValues(values)

		continue_entities = raw_input("Do you want to create another entity? (Y/N) ")
		if continue_entities == 'n' or continue_entities == 'N':
			continue_entities = 'x'
			break
		continue_entities = raw_input("Enter an entity name ('x' to quit): ")

def getValues(values):
	print "Get your values here!"

#Create Entity (maybe from keywords)
#Add Value
#Get Synonyms

app()