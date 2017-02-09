import sys

array = [0] * 1000

previousWhile = 0

dataPtr = 0

prgPtr = 0

def parse(program):
	global array
	global dataPtr
	global prgPtr
	while(program):
		def goto():
			global array
			global dataPtr
			global prgPtr
			try:
				if dataPtr < 0:
					dataPtr = 0
					print("Pointer has been reset to zero because it was negative.")
				if prgPtr < 0:
					print("Fatal Error: Instruction Pointer less than zero")
					quit()
				print("Eval")
				eval(program[prgPtr], program)
			except(IndexError):
				print("Extending")
				array.extend([0] * 1000)
				goto()
			except(ValueError):
				pass
		goto()
		if prgPtr == len(program):
			break
		prgPtr += 1

def increment(x):
	return x + 1

def decrement(x):
	return x - 1

def beginLoop():
	global array
	global dataPtr
	global prgPtr
	global previousWhile
	if array[dataPtr] == 0: 
		for x, item in enumerate(program): 
			if item == "]": 
				previousWhile = prgPtr
				prgPtr = x + 1

def closeLoop():
	global array
	global dataPtr
	global prgPtr
	global previousWhile
	if array[dataPtr] != 0: 
		prgPtr = previousWhile;

def eval(x, program):
	global array
	global dataPtr
	global prgPtr
	global previousWhile
	command = {
		">" : increment(dataPtr),
		"<" : decrement(dataPtr),
		"+" : increment(array[dataPtr]),
		"-" : decrement(array[dataPtr]),  
		"." : print(array[dataPtr]),
		"," : sys.stdin.read(1),
		"[" : beginLoop(), 
		"]" : closeLoop(), 
	}.get(x, ValueError) 

	return command()

def main():
	"""Interpreter debugging"""
	pass

if __name__ == "__main__":
	main()