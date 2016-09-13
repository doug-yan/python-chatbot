from values import getValues as get_values

def getEntities():
	jsonString = ''
	entity = raw_input("Enter an entity name ('q' to quit): ")

	while entity != 'q':
		jsonString += '{"entity":"'
		jsonString += entity
		jsonString += '","values":['
		jsonString += get_values()
		jsonString += '],"open_list":false,"description":null},'

		entity = raw_input("Do you want to create another entity? (Y/N) ")
		if entity == 'n' or entity == 'N':
			break
		entity = raw_input("Enter an entity name ('q' to quit): ")

	jsonString = jsonString[:-1]
	jsonString += '],'
	return jsonString