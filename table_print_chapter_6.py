#! Python3
# a table printing script for text in Chapter 6

# check if any content in the table data
def check_content(items, column, raw):
    try:
        items[column][raw]
        return True
    except IndexError:
        return False

def print_table(items, columns, raws, col_widths):
    # draw the table
    for k in range(0, raws):
        for v in range(0, columns):
            print('| ' + items[v][k].rjust(col_widths[v]), end='')
        print('|\n')

# find out the longest words and return iss length as column width
def longest_words(items, column):
    length = 0
    for i in range(0, len(items[column])):
        if length < len(items[column][i]):
            length = len(items[column][i])
    return length

# define table data
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# define column number
col_num = len(table_data)

# define raw number
raw_num = 0
for i in range(0, len(table_data)):
    if raw_num < len(table_data[i]):
        raw_num = len(table_data[i])

# add '' to make each column the same number of content
for i in range(0, raw_num):
    for j in range(0, col_num):
        if check_content(table_data, j, i) == False:
            table_data[j] += ['']

# define width for each column
col_widths = []
for i in range(0, len(table_data)):
    col_widths = col_widths + [longest_words(table_data, i)]

# print table
print_table(table_data, col_num, raw_num, col_widths)
