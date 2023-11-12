def sequential_search(n,target,array):
    for i in range(n):
        if(array[i] == target):
            return i + 1

data = input().split()
n = int(data[0])
target = data[1]
array = input().split()

print(sequential_search(n,target,array))