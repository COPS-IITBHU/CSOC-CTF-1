def fibonacci(n):
        x = [0,1]
        if n == 1:
                return [0]
        elif n ==2 :
                return [0,1]
        else:
                for i in range(2,n+1):
                        x.append(x[i-2]+x[i-1])
                return x

def f(n):
	s = [0]
	fib = fibonacci(n)
	for i in range(1,len(fib)):
		s.append(int(str(s[i-1]) + str(fib[i])) % 10**11)
	return sum(s[1:]) % 10**11
