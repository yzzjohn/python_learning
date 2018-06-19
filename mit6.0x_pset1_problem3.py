#! Python3
# a script to find out the longest substring of 's'
# in which the letters occur in alphabetical order
#
# problem 3 for pset1 of mit6.0x on edx.org


# initial a list to store substrings in alphabetical order
list = []

# seperate 's' to substrings in alphabetical order
for i in range(0,len(s)):
    if i == 0:
        string = s[i]
    else:
        if ord(s[i]) >= ord(s[i - 1]):
            string += s[i]
        else:
            list.append(string)
            string = s[i]

# when the whole string is in alphabetical order
if list == []:
    list.append(s)

# find out the longest substring
length = 0
for i in range(0, len(list)):
    if len(list[i]) > length:
        length = len(list[i])
        index = i

print('Longest substring in alphabetical order is: ' + list[index])
