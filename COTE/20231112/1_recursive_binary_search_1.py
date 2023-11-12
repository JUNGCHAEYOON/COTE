def binary_search(array,target,start,end):
    if(start > end):
        return None
    mid = int((start + end)/2)
    if(array[mid] == target):
        return mid
    elif(array[mid] < target):
        return binary_search(array,target,mid+1,end)
    else:
        return binary_search(array,target,start,mid-1)

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,len(array)-1)
print(result + 1,"번째")