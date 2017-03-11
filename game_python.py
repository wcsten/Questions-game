import random


def sort_questions(dict_tiger, dict_bear, dict_turtle):
	list_question = []

	question_number_tiger = random.randint(1, len(dict_tiger))
	question_number_tiger -= 1

	question_number_bear = random.randint(1, len(dict_bear))
	question_number_bear -= 1

	question_number_turtle = random.randint(1, len(dict_turtle))
	question_number_turtle -= 1

	for index, obj in enumerate(dict_tiger):
		if index == question_number_tiger:
			list_question.append(obj)
			dict_tiger.remove(obj)
			break

	for index, obj in enumerate(dict_bear):
		if index == question_number_bear:
			list_question.append(obj)
			dict_bear.remove(obj)
			break

	for index, obj in enumerate(dict_turtle):
		if index == question_number_turtle:
			list_question.append(obj)
			dict_turtle.remove(obj)
			break

	return list_question


def choice_one_question(choice, list_question):
	for index, obj in enumerate(list_question):
		if index == choice:
			return obj
	return None


if __name__ == '__main__':

	list_tiger = [
		{'question': 'tiger 1', 'category':'1'},
		{'question': 'tiger 2', 'category':'1'},
		{'question': 'tiger 3', 'category':'1'},
		{'question': 'tiger 4', 'category':'1'},
		{'question': 'tiger 5', 'category':'1'},
	]

	list_bear = [
		{'question': 'bear 1', 'category':'2'},
		{'question': 'bear 2', 'category':'2'},
		{'question': 'bear 3', 'category':'2'},
		{'question': 'bear 4', 'category':'2'},
		{'question': 'bear 5', 'category':'2'},
	]

	list_turtle = [
		{'question': 'turtle 1', 'category':'3'},
		{'question': 'turtle 2', 'category':'3'},
		{'question': 'turtle 3', 'category':'3'},
		{'question': 'turtle 4', 'category':'3'},
		{'question': 'turtle 5', 'category':'3'},
	]

	result_list = []
	email = input('Informe seu email para começar:')

	#1
	sorted_list1 = sort_questions(list_tiger, list_bear, list_turtle)
	for item_dict in sorted_list1:
		print(item_dict.get('question'))

	choice1 = int(input('Escolha uma questão entre 1 e 3:'))
	choice1 -= 1
	second_answer1 = choice_one_question(choice1, sorted_list1)
	result_list.append(second_answer1)

	#2
	sorted_list2 = sort_questions(list_tiger, list_bear, list_turtle)
	for item_dict in sorted_list2:
		print(item_dict.get('question'))

	choice2 = int(input('Escolha uma questão entre 1 e 3:'))
	choice2 -= 1
	second_answer2 = choice_one_question(choice2, sorted_list2)
	result_list.append(second_answer2)

	#3
	sorted_list3 = sort_questions(list_tiger, list_bear, list_turtle)
	for item_dict in sorted_list3:
		print(item_dict.get('question'))

	choice3 = int(input('Escolha uma questão entre 1 e 3:'))
	choice3 -= 1
	second_answer3 = choice_one_question(choice3, sorted_list3)
	result_list.append(second_answer3)

	#4
	sorted_list4 = sort_questions(list_tiger, list_bear, list_turtle)
	for item_dict in sorted_list4:
		print(item_dict.get('question'))

	choice4 = int(input('Escolha uma questão entre 1 e 3:'))
	choice4 -= 1
	second_answer4 = choice_one_question(choice4, sorted_list4)
	result_list.append(second_answer4)

	#5
	sorted_list5 = sort_questions(list_tiger, list_bear, list_turtle)
	for item_dict in sorted_list5:
		print(item_dict.get('question'))

	choice5 = int(input('Escolha uma questão entre 1 e 3:'))
	choice5 -= 1
	second_answer5 = choice_one_question(choice5, sorted_list5)
	result_list.append(second_answer5)
	

	for item_dict in result_list:
		question = item_dict.get('question')
		print(question)


	database_path = 'banco_de_questoes/{}.csv'.format(email) 

	with open(database_path, 'w') as file:
		for item_dict in result_list:
			line = '{},{}\n'.format(item_dict.get('question'), item_dict.get('category'))
			file.write(line)

