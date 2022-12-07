#!/usr/bin/python3
# cd'e rundt i filsystemet, kjøre ls og akkumulere størrelsene på mappene

from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

for line in open('7.input'):
	match line.split():
		case '$', 'cd', '/': curr = ['']
		case '$', 'cd', '..': curr.pop()
		case '$', 'cd', x: curr.append(x+'/')
		case '$', 'ls': pass
		case 'dir', _: pass
		case size, _:
			for p in accumulate(curr):
				dirs[p] += int(size)

print("Summen av alle mappene som er mindre eller lik 100'000 er: " + 
		str(sum(s for s in dirs.values() if s <= 100_000)))

print("Den minste mappen som kan slettes for å få nok ledig plass (30'000'000) er: " + 
		str(min(s for s in dirs.values() if s >= dirs[''] - 40_000_000)))
