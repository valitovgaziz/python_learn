def parrot(voltage, state='a staff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

b = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**b)
