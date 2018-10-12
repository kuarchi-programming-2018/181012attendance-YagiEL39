def fib(n):
	a,b=0,1
	if n==0:
		return 0
	else:
		for i in range(n):
			a,b=b,a+b
		return b

print(fib(int(input())))
print(fib(2108))
		