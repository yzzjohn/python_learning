#! Python3
# a regex version of ".strip()" for test in Chapter 7

import re

def re_strip(string, char):
    if char == '':
        # remove blanket at beginning/end
        remove_blank = re.compile(r'(^\s*)(\w+[A-Za-z0-9\s]*\w+)(\s*$)')
        mo = remove_blank.search(string)
        output = mo.group(2)
        return output
    else:
        # remove select characters
        remove_character = re.compile(r'%s'%character)
        output = remove_character.sub('', string)
        return output

# ask for string to modify
print('Please enter a string:')
string = input()

# ask for character to remove
print('Please enter the charter you want to remove')
character = input()

# print result
print(re_strip(string, character))
