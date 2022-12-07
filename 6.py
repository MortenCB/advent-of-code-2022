#!/usr/bin/python3

signal = open('6.input', 'r').read().strip()
signalFound = False

for i in range(4, len(signal)):
	if not signalFound:
		s = signal[i-4:i]
		if len(set(s)) == 4:
			print("First start-of-packet marker is at " + str(i))
			signalFound = True	

	m = signal[i-14:i]
	if len(set(m)) == 14:
		print("First start-of-message marker is at " + str(i))
		break
