#!/usr/bin/python3
from functools import partial
import math

lines = open('8.input', 'r').read().splitlines()

grid = []
for y,row in enumerate(lines):
	grid.append(list(map(int,row)))

cols = list(zip(*grid))

def views(x,y):
	# Returnerer utsikten i 4 retninger fra en gitt posisjon
	# Rekkefølgen er over, venstre, høyre og under
	# Ellers er rekkefølgen som man ser det fra posisjonen gitt som input
	over = cols[x][:y]
	venstre = grid[y][:x]
	høyre = grid[y][x+1:]
	under = cols[x][y+1:]
	return [over[::-1], venstre[::-1], høyre, under]

def retning_score(hus, retning):
	# Returnerer scoren for utsikten for en gitt retning
	score = 0
	for i in retning:
		score += 1
		if i >= hus:
			break
	return score

visibleTrees = 0
utsiktScore = 0

for y, row in enumerate(grid):
	for x, hus in enumerate(row):
		if any(hus > max(other or [-math.inf]) for other in views(x,y)):
			visibleTrees += 1
		retn_score = partial(retning_score, hus)
		score = math.prod(map(retn_score, views(x,y)))
		if score > utsiktScore:
			utsiktScore = score

print("Antall trær som er synlig fra utsiden av grid'en: " + str(visibleTrees))

print("Den beste utsikten har score: " + str(utsiktScore))
