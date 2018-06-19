############################################################
#                                                          #
# This is a python script for Collatz Sequence #
# It's a test script for python learning                   #
#                                                          #
#                                                          #
# Author: John Zhu                                         #
# Date: 2018/03/21                                         #
#                                                          #
############################################################


def check_input(user_input):
	try:
		int(user_input)
		return True
	except ValueError:
		return False

def collatz(number):
	if number % 2 == 0:
		number = number // 2
	else:
		number = number * 3 + 1
	print(number)
	return number

print('please enter an integer: ')

# ask for imput and collatz #
while True:
	user_input = input()
	if check_input(user_input) == True:
		break
	print('Wrong input, please enter an integer: ')

output = int(user_input)

while True:
	output = collatz(output)
	if output == 1:
		break