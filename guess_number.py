# This is a test python script for python learning #

import random

def check_input(user_input):
	try:
		int(user_input)
		return True
	except ValueError:
		return False

def compare_guess(num):
	if num < number:
		print('Your guess is too low')
		return False
	elif num > number:
		print('Your guess is too high')
		return False
	else:
		print('Good Job! You guessed my number in ' + str(count) + ' guesses!')
		return True

# random a number to be guessed#
number = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')



# ask for guess and count guess times #
for count in range(1, 20):
	print('Take a guess.')
	
	# check if the inpur is valid #
	while True:
		guess = input()
		if check_input(guess) == True:
			break
		print('Please enter a number: ')

	guess_num = int(guess)

	if compare_guess(guess_num) == True:
		break
