import json
from keywords import getKeywords as get_keywords
from entities import getEntities as get_entities

def app():
	#create value and add to list 
	#for each value, find synonyms, add to list (optional, use can choose which synonyms to add to list)
	#export list of entities, values, and synonyms
	entity = ''
	values = []

	#Use AlchemyAPI to get keywords so that users can get an idea for what kind of entities they should create
	get_analysis = raw_input("Would you like to use a few sentences to help you come up with entities? (Y/N) ")
	if get_analysis == 'y' or get_analysis == 'Y':
		get_keywords()

	#Users create entities and values, and then get synonyms to those values
	get_entities(entity, values)

app()