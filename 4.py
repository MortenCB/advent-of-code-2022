#!/usr/bin/python3
import re

lines = open('4.input', 'r').read().strip().split('\n')

total = 0
for line in lines:
	a, b, c, d = map(int, re.findall('\d+', line))
	if a <= c and b >= d or c <= a and d >= b:
		total += 1

print('Number of assignment pairs where one range fully contains the other: ' + str(total))

total = 0
for line in lines:
	a, b, c, d = map(int, re.findall('\d+', line))
	if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
		total += 1

print('Number of assignment pairs that overlaps: ' + str(total))
