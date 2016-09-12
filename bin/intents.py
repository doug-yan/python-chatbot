import unirest
# response = unirest.get("https://wordsapiv1.p.mashape.com/words/vegetabels/hasTypes",
#   headers={
#     "X-Mashape-Key": "MAj5SaQJGYmsh4WS1zpILm5h3EhMp1QG1ZNjsnripE92FdtaSD",
#     "Accept": "application/json"
#   }
# )

def createIntent():
	intent_name = raw_input("Enter the intent name ('q' to quit): ")
	training_data = []
	num_data_points = 0
	quit = False
	force_quit = 'n'

	while intent_name != 'q':
		data_point = raw_input("Enter a piece of training data. " + str(6-num_data_points) + " more pieces required ('q' to quit): ")
		if data_point == 'q':
			force_quit =  raw_input("At least 6 pieces of training data are required! Are you sure you want to quit? (Y/N) ")

		while data_point != 'q' or force_quit == 'n' or force_quit == 'N':
			num_data_points += 1
			if quit == False:
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

		print "The intent name is: " + intent_name
		print "The training data is: "
		for i in range(0, len(training_data)):
			print training_data[i]

		intent_name = raw_input("Do you want to create another intent? (Y/N) ")
		if intent_name == 'n' or intent_name == 'N':
			break

		intent_name = raw_input("Enter the intent name ('q' to quit): ")
