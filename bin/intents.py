def getIntent():
	intent_name = raw_input("Enter the intent name ('q' to quit): ")
	quit = False
	force_quit = 'n'
	jsonString = ''

	while intent_name != 'q':
		num_data_points = 0
		training_data = []
		data_point = raw_input("Enter a piece of training data. " + str(6-num_data_points) + " more pieces required ('q' to quit): ")
		if data_point == 'q':
			force_quit =  raw_input("At least 6 pieces of training data are required! Are you sure you want to quit? (Y/N) ")

		jsonString += '{"intent":"'
		jsonString += intent_name
		jsonString += '",'
		jsonString += '"examples":['

		while data_point != 'q' or force_quit == 'n' or force_quit == 'N':
			num_data_points += 1
			if quit == False and data_point != 'q' and data_point != 'Q':
				training_data.append(data_point)

			if num_data_points >= 6:
				data_point = raw_input("Enter a piece of training data ('q' to quit): ")
				if data_point == 'q':
					break

			else:
				data_point = raw_input("Enter a piece of training data. " + str(6-num_data_points) + " more pieces required ('q' to quit): ")
				if data_point == 'q' and num_data_points < 6:
					num_data_points -= 1
					quit = True
					force_quit = raw_input("At least 6 pieces of training data are required! Are you sure you want to quit? (Y/N) ")
					if force_quit == 'y' or force_quit == 'Y':
						break

					else:
						quit = False

		for i in range(0, len(training_data)):
			jsonString += '{"text":"'
			jsonString += training_data[i]
			if i < len(training_data) - 1:
				jsonString += '"},'
			else:
				jsonString += '"}'
		jsonString += '],"description":null},'

		intent_name = raw_input("Do you want to create another intent? (Y/N) ")
		if intent_name == 'n' or intent_name == 'N':
			break

		intent_name = raw_input("Enter the intent name ('q' to quit): ")

	jsonString = jsonString[:-1]
	jsonString += '],'
	return jsonString