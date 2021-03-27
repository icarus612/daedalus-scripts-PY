import sys
r = int(sys.argv[1]) if len(sys.argv) == 2 else 1
x = [] 
def next_num(n):
    yield n
    yield from next_num(n+1)

s = next_num(2)
def get_next_prime(s):
    n = next(s)
    yield n 
    yield from get_next_prime(i for i in s if i % n != 0)

p = get_next_prime(s)
for i in range(r):
    x.append(next(p))

print(x)