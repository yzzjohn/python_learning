#! Python3
# a script to prints the number of times the string 'bob' occurs in 's'
#
# problem 2 for pset1 of mit6.0x on edx.org

count = 0
key_word = 'bob'
for i in range(len(s) - 2):
    if s[i] + s[i+1] + s[i+2] == key_word:
        count += 1
print('Number of times bob occurs is: ' + str(count))
