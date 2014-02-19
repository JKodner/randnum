"""Assignment: Make a program that takes in random numbers from the range from -500000 to 1 million and prints 3 numbers if they add up to 0."""
import random
num = range(-500000, 1000001)
my_list = []
while len(my_list) < 1000001:
	rand_num = random.choice(num)
	my_list.append(rand_num)
count = 0
for x in my_list:
	for y in my_list:
		for z in my_list:
			if x + y + z == 0:
				count += 1
				print '-*-'
				print "Set #%d:" % count
				print x
				print y
				print z
				print '-*-'
				print " "
			else:
				None