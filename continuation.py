x = 0

def continuation():
	global x
	while(x < 10):
		def inc():
			x += 1
		inc()
		print(x)
	print(x)