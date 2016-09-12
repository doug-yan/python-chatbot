from values import getValues as get_values

def getEntities(entity, values):
	jsonString = ''
	entity = raw_input("Enter an entity name ('q' to quit): ")

	while entity != 'q':
		get_values(entity, values)

		entity = raw_input("Do you want to create another entity? (Y/N) ")
		if entity == 'n' or entity == 'N':
			break
		entity_input = raw_input("Enter an entity name ('q' to quit): ")

	return jsonString