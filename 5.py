#!/usr/bin/python3

with open('5.input', 'r') as f:
   lines = [line.rstrip('\n') for line in f]

crateLines = 0

# Figure out how many lines of crates we have:
for l in lines:
	if l.startswith(' 1'):
		break
	crateLines += 1

print("Number of lines with crates: " + str(crateLines))

numStacks = lines[crateLines].strip()[-1:]

print("Number of stacks: " + str(numStacks))

stacks = [[] for _ in range(int(numStacks))]

# Legge inn innhold i crate-stackene, første element er den nederste craten:
for l in lines[0:int(numStacks)]:
	for i, c in enumerate(l[1::4]):
		if not c.isspace():
			stacks[i].insert(0,c)

stacks2 = [s[:] for s in stacks]

# Gå gjennom alle kommandolinjene og flytte bokser:
for l in lines[crateLines+2:]:
	count,fro,to = l.split(' ')[1::2]

	for i in range(int(count)):
		stacks[int(to)-1].append(stacks[int(fro)-1].pop())

	stacks2[int(to)-1].extend(stacks2[int(fro)-1][-int(count):])
	stacks2[int(fro)-1] = stacks2[int(fro)-1][:-int(count)]

print("Top crates i oppgave 1: ", "".join(s[-1] for s in stacks))

print("Top crates i oppgave 2: ", "".join(s[-1] for s in stacks2))
