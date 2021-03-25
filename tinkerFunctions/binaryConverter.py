import sys
import math


x, y = int(sys.argv[1]), int(sys.argv[1])

if x == 0: 
	print(0)
else: 
	b = 0
	r = []
	while x >= 1:
		b+=1
		x/=2

	for i in range(b, 0, -1):
		if y >= 2**(i-1):
			r.append('1')
			y -= 2**(i-1)
		else:
			r.append('0')

	print("".join(r))