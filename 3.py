#!/usr/bin/python3
import string

lines = open('3.input', 'r').read().strip().split('\n')

result = 0
for line in lines:
	a, b = line[:len(line)//2], line[len(line)//2:]
	same = (set(a) & set(b)).pop()
	result += string.ascii_letters.index(same) + 1

print('The sum of the priorities is: ' + str(result))

result = 0
for i in range(0, len(lines), 3):
	a, b, c = lines[i:i+3]
	same = (set(a) & set(b) & set(c)).pop()
	result += string.ascii_letters.index(same) + 1

print('The sum of the priorities of those item types is: ' + str(result))
