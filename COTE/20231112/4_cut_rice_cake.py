import sys

n,target = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

def function(array,target,cutter):
    total = 0
    for i in array:
        rest = i - cutter if(i - cutter > 0) else 0
        total += rest
    if(total >= target):
        return cutter
    else:
        return function(array,target,cutter-1)

print(function(array,target,max(array)))
