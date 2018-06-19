#! Python3
# a script to count vowels in the string 's'
#
# problem 1 in pset1 of mit6.0x on edx.org

count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print('Number of vowels: ' + str(count))
