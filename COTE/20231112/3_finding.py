import sys

def function(array,finder,start,end):
    if(start > end):
        return "no"
    mid = int((start + end)/2)
    if(finder == array[mid]):
        return "yes"
    elif(finder < array[mid]):
        return function(array,finder,start,mid-1)
    else:
        return function(array,finder,mid+1,end)


n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
find_array = list(map(int,sys.stdin.readline().split()))

for finder in find_array:
    print(function(array,finder,0,len(array)-1),end=" ")
