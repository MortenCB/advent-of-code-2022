#!/usr/bin/python3

with open('1.input', 'r') as f:
	all_elves_total = []
	for elfgroup in f.read().strip().split('\n\n'):
		elf_total = sum(int(calorie) for calorie in elfgroup.split('\n'))
		all_elves_total.append(elf_total)
	all_elves_total.sort()

print('The elf with the most calories carry ' + str(all_elves_total[-1]))

print('The sum of the 3 elves with the most calories carried: ' + str(sum(all_elves_total[-3:])))
