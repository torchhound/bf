import sys

array = [0] * 1000

ptr = 0

def parse(program):
	global commands
	global array
	global ptr
	while(program):
		try:
			def goto():
				eval(program[0])
				program = program[1:]
			goto()
		except(IndexError):
			array.extend([0] * 1000)
			goto()


def eval(x):
	return {
		">" : ptr += 1,
		"<" : ptr -= 1,
		"+" : array[ptr] += 1,
		"-" : array[ptr] -= 1,  
		"." : print(array[ptr]),
		"," : sys.stdin.read(),
		"[" : , #make while loop
		"]" : , #close while loop
	}.get(x, ValueError) #pass instead of ValueError

def main():
	"""Interpreter debugging"""
	pass

if __name__ == "__main__":
	main()