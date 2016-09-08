import json
from thesaurus import thesaurus as get_syn
from keywords import getKeywords as get_keywords

def app():
	#create value and add to list 
	#for each value, find synonyms, add to list (optional, use can choose which synonyms to add to list)
	#export list of entities, values, and synonyms

	entities = []
	values = []

	#Use AlchemyAPI to get keywords so that users can get an idea for what kind of entities they should create
	get_analysis = raw_input("Would you like to use a few sentences to help you come up with entities? (Y/N) ")
	if get_analysis == 'y' or get_analysis == 'Y':
		get_keywords()

	#Users create entities and values, and then get synonyms to those values
	getEntities(entities, values)


def getEntities(entities, values):
	continue_entities = raw_input("Enter an entity name ('q' to quit): ")
	entity_index = 0
	while continue_entities != 'q':
		entities.append(continue_entities)
		getValues(values)

		continue_entities = raw_input("Do you want to create another entity? (Y/N) ")
		if continue_entities == 'n' or continue_entities == 'N':
			continue_entities = 'q'
			break
		continue_entities = raw_input("Enter an entity name ('q' to quit): ")

def getValues(values):
	print 'here in values!'

#Create Entity (maybe from keywords)
#Add Value
#Get Synonyms

app()