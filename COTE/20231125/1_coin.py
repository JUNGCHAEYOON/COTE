import sys

n,k = map(int,sys.stdin.readline().split())

array = []
for i in range(n):
    coin = int(sys.stdin.readline())
    array.append(coin)

array.sort(reverse=True)

count = 0
for coin in array:
    if(coin > k):
        continue
    count += (k // coin)
    k = k % coin

print(count)