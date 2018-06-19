#! Python3
# Test Chapter 5


# initialize your items in pocket and the loot for defeating a dragon
your_item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# a function to display player's currrent items
def display_inventory(inventory):
	total_item = 0
	print('Intentory: ')
	for k, v in inventory.items():
		print(str(v) + ' ' + str(k))
		total_item += v
	print('Total number of items: ' + str(total_item))

# a function to add loots when defeating monsters
def add_to_inventory(inventory, loot):
	for i in range(0, len(loot)):
		inventory.setdefault(loot[i], 0)
		inventory[loot[i]] += 1

# welcom words
print('Welcome to the Dungeon!')

# ask for player's action
while True:
	print('Press \"I\" to check your bag; press \"C\" to continue; press \"Q\" to quit')
	a = input()

	if a == 'i':
		display_inventory(your_item)

	elif a == 'c':
		print('You defeated a dragon and got lots of loots!')
		add_to_inventory(your_item, dragon_loot)

	elif a == 'q':
		break

	else:
		print('Opps, wrong input')

# end game and print out player's items
print('Here is what you got.')
display_inventory(your_item)
