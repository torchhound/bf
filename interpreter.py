import sys

array = [0] * 1000

ptr = 0

def parse(program):
	global array
	global ptr
	while(program):
		def goto():
			try:
				eval(program[0])
			except(IndexError):
				array.extend([0] * 1000)
				goto()
			except(ValueError):
				pass
		goto()
		program = program[1:]


def eval(x):
	global array
	global ptr
	command = {
		">" : lambda _: ptr += 1,
		"<" : lambda _: ptr -= 1,
		"+" : lambda _: array[ptr] += 1,
		"-" : lambda _: array[ptr] -= 1,  
		"." : lambda _: print(array[ptr]),
		"," : lambda _: sys.stdin.read(),
		"[" : lambda _: , #make while loop
		"]" : lambda _: , #close while loop
	}.get(x, ValueError) #pass instead of ValueError? [x]() instead of get? and use a try except block instead of default in .get()?

	return command()

def main():
	"""Interpreter debugging"""
	pass

if __name__ == "__main__":
	main()