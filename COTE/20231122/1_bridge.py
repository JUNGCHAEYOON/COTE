import sys
t = int(sys.stdin.readline())

def fac(n):
    if(n == 1):
        return 1
    return n * fac(n-1)

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = 1
    for i in range(n):
        result *= m
        m -= 1
    result //= fac(n)
    print(result)

