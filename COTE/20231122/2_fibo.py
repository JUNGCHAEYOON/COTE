import sys

n = int(sys.stdin.readline())

fibCount = 0
fibonacciCount = 0
def fib(n):
    global fibCount
    if(n == 1 or n == 2):
        fibCount += 1
        return n
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    global fibonacciCount
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[n] = d[n-1] + d[n-2]
        fibonacciCount += 1
    return d[n]

fib(n)
fibonacci(n)

print(fibCount)
print(fibonacciCount)


