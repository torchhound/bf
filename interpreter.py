import sys

array = [0] * 1000

previousWhile = 0

dataPtr = 0

prgPtr = 0

def parse(program):
	global array
	global dataPtr
	global prgPtr
	while(prgPtr <= len(program)):
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
				eval(program[prgPtr], program)
			except IndexError as e:
				print(e)
				array.extend([0] * 1000)
				goto()
			except ValueError as e:
				print(e)
				pass
		goto()
		prgPtr += 1

def increment(x):
	x = x + 1
	return x 

def decrement(x):
	x = x - 1
	return x

def beginLoop(program):
	global array
	global dataPtr
	global prgPtr
	global previousWhile
	if array[dataPtr] == 0: 
		for x, item in enumerate(program): 
			if item == "]": 
				previousWhile = prgPtr
				prgPtr = x + 1

def closeLoop(program):
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
		">" : lambda _: increment(dataPtr),
		"<" : lambda _: decrement(dataPtr),
		"+" : lambda _: increment(array[dataPtr]),
		"-" : lambda _: decrement(array[dataPtr]),  
		"." : lambda _: print(array[dataPtr]),
		"," : lambda _: sys.stdin.read(1),
		"[" : lambda _: beginLoop(program), 
		"]" : lambda _: closeLoop(program), 
	}.get(x, ValueError)

	print(command(0))

	return command(0)

def main():
	"""Interpreter debugging"""
	pass

if __name__ == "__main__":
	main()