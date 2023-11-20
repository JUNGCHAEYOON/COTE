import sys

n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline()))

total = 0
for i in range(len(k)):
    if(k[i] == max(k)):
        if(k[i-1] != -1 and k[i+1] != -1):
            total += k[i]
            k[i] = -1

print(total)