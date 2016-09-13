import json
from intents import getIntent as get_intent
from keywords import getKeywords as get_keywords
from entities import getEntities as get_entities

def app():
	file = open('data.json','w')
	json_string = '{"name":"'

	conversation_name = raw_input("Enter a name for this conversation: ")
	description = raw_input("Enter a description for this conversation: ")

	json_string += conversation_name
	json_string += '", '
	json_string += '"intents":['
	#Get intent and training data from user
	json_string += get_intent()

	#Use AlchemyAPI to get keywords so that users can get an idea for what kind of entities they should create
	get_analysis = raw_input("Would you like to use a few sentences to help you come up with entities? (Y/N) ")
	if get_analysis == 'y' or get_analysis == 'Y':
		get_keywords()

	#Users create entities and values, and then get synonyms to those values
	json_string += '"entities":['
	json_string += get_entities()


	json_string += '"language:":"en","metadata":null,"description":"' 
	json_string += description
	json_string += '",'
	json_string += '"dialog_nodes":[]}'

	json_obj = json.dumps(json_string)

	file.write(json_string)

app()