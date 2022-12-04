#!/usr/bin/python3

rounds = open('2.input', 'r').read().strip().split('\n')

points = {
	"A X": 4,
	"A Y": 8,
	"A Z": 3,
	"B X": 1,
	"B Y": 5,
	"B Z": 9,
	"C X": 7,
	"C Y": 2,
	"C Z": 6,
}
score = sum([points[round] for round in rounds])

print('Part 1: My total score would be: ' + str(score))

points = {
	"A X": 0 + 3,
	"A Y": 3 + 1,
	"A Z": 6 + 2,
	"B X": 0 + 1,
	"B Y": 3 + 2,
	"B Z": 6 + 3,
	"C X": 0 + 2,
	"C Y": 3 + 3,
	"C Z": 6 + 1,
}

score = sum([points[round] for round in rounds])

print('Part 2: My total score would be: ' + str(score))
