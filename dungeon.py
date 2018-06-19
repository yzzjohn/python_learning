# Test Chapter 5

your_item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
	total_item = 0
	print('Intentory: ')
	for k, v in inventory.items():
		print(str(v) + ' ' + str(k))
		total_item += v
	print('Total number of items: ' + str(total_item))

def add_to_inventory(inventory, loot):
	for i in range(0, len(loot)):
		inventory.setdefault(loot[i], 0)
		inventory[loot[i]] += 1

print('Welcome to the Dungeon!')

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

print('Here is what you got.')
display_inventory(your_item)



