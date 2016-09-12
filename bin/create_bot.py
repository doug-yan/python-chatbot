import json
from intents import getIntent as get_intent
from keywords import getKeywords as get_keywords
from entities import getEntities as get_entities

def app():
	entity = ''
	values = []
	jsonString = '{"name":"'

	conversation_name = raw_input("Enter a name for this conversation: ")

	jsonString += conversation_name
	jsonString += '", '

	#Get intent and training data from user
	jsonString += get_intent()

	#Use AlchemyAPI to get keywords so that users can get an idea for what kind of entities they should create
	get_analysis = raw_input("Would you like to use a few sentences to help you come up with entities? (Y/N) ")
	if get_analysis == 'y' or get_analysis == 'Y':
		get_keywords()

	#Users create entities and values, and then get synonyms to those values
	jsonString += get_entities(entity, values)

	jsonString += '}'

	json_obj = json.loads(jsonString)
	print (json.dumps(json_obj, indent=2))

	# print jsonString

app()