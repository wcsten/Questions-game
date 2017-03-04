import random


def sort_questions(list_tiger, list_bear, list_turtle):
	list_question = []

	question_number_tiger = random.randint(1, len(list_tiger))
	question_number_tiger -= 1

	question_number_bear = random.randint(1, len(list_bear))
	question_number_bear -= 1

	question_number_turtle = random.randint(1, len(list_turtle))
	question_number_turtle -= 1

	for index, obj in enumerate(list_tiger):
		print('for tiger')
		if index == question_number_tiger:
			list_question.append(obj)
			list_tiger.remove(obj)
			break

	for index, obj in enumerate(list_bear):
		print('for bear')
		if index == question_number_bear:
			list_question.append(obj)
			list_bear.remove(obj)
			break

	for index, obj in enumerate(list_turtle):
		print('for turtle')
		if index == question_number_turtle:
			list_question.append(obj)
			list_turtle.remove(obj)
			break

	return list_question


def choice_one_question(choice, list_question):
	for index, obj in enumerate(list_question):
		if index == choice:
			return obj
	return None


if __name__ == '__main__':

	list_tiger = [
		'tiger 1',
		'tiger 2',
		'tiger 3',
		'tiger 4',
		'tiger 5',
	]

	list_bear = [
		'bear 1',
		'bear 2',
		'bear 3',
		'bear 4',
		'bear 5',
	]

	list_turtle = [
		'turtle 1',
		'turtle 2',
		'turtle 3',
		'turtle 4',
		'turtle 5',
	]

	result_list = []
	#1
	sorted_list1 = sort_questions(list_tiger, list_bear, list_turtle)
	print(sorted_list1)
	choice1 = int(input('Escolha uma questão entre 1 e 3:'))
	choice1 -= 1
	second_answer1 = choice_one_question(choice1, sorted_list1)
	result_list.append(second_answer1)

	#2
	sorted_list2 = sort_questions(list_tiger, list_bear, list_turtle)
	print(sorted_list2)
	choice2 = int(input('Escolha uma questão entre 1 e 3:'))
	choice2 -= 1
	second_answer2 = choice_one_question(choice2, sorted_list2)
	result_list.append(second_answer2)

	#3
	sorted_list3 = sort_questions(list_tiger, list_bear, list_turtle)
	print(sorted_list3)
	choice3 = int(input('Escolha uma questão entre 1 e 3:'))
	choice3 -= 1
	second_answer3 = choice_one_question(choice3, sorted_list3)
	result_list.append(second_answer3)

	#4
	sorted_list4 = sort_questions(list_tiger, list_bear, list_turtle)
	print(sorted_list4)
	choice4 = int(input('Escolha uma questão entre 1 e 3:'))
	choice4 -= 1
	second_answer4 = choice_one_question(choice4, sorted_list4)
	result_list.append(second_answer4)

	#5
	sorted_list5 = sort_questions(list_tiger, list_bear, list_turtle)
	print(sorted_list5)
	choice5 = int(input('Escolha uma questão entre 1 e 3:'))
	choice5 -= 1
	second_answer5 = choice_one_question(choice5, sorted_list5)
	result_list.append(second_answer5)



	print(result_list)





































second_list_question = choice_one_question(1, ['bla', 'ble', 'bli'])

choice = 1
a_list = ['bla', 'ble', 'bli']

second_list_question = choice_one_question(choice, a_list)

	
	
def choice_one_question(choice, a_list):
	second_list_question = []

	for index, obj in enumerate(a_list):
		if index == choice:
			second_list_question.append(obj)

	return second_list_question
