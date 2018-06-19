#! Python3
# a password strength checker for test in Chapter 7

import re, sys

# define password rules: longer than 8 and contain 1 uppercase, 1 lowercase and 1 digit at least
pw_length = re.compile(r'\w{8,}')
pw_strength = re.compile(r'\w*[A-Z]+\w*\d+\w*[a-z]+\w*|\w*[A-Z]+\w*[a-z]+\w*\d+\w*|\w*[a-z]+\w*[A-Z]+\w*\d+\w*|\w*[a-z]+\w*\d+\w*[A-Z]+\w*|\w*\d+\w*[a-z]+\w*[A-Z]+\w*')

# check length
def check_length(pw):
    mo = pw_length.search(pw)
    if mo == None:
        return False
    else:
        return True

# check characters and digits
def check_strength(pw):
    mo = pw_strength.search(pw)
    if mo == None:
        return False
    else:
        return True

# print introduction
print('''This is a password strength checker.

A good password should be longer than 8 chars and contain 1 uppercase, 1 lowercase and 1 digit at least.

This app will help to check if your password is strong enough.
''')

# keep asking input untill user choose to quit
while True:
    print('Enter your password, or press \"q\" to quit: ', end='')
    password = input()

    # quit while pressing "q"
    if password == 'q':
        sys.exit()

    # check password's strength and print result
    if check_length(password) == True and check_strength(password) == True:
        print('Great! Your password is strong enough!')
    else:
        print('Oops, you\'d better change your password.')
