n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

def sortUpToDown(data):
    answer = sorted(data,reverse=True)
    return answer

for i in sortUpToDown(data):
    print(i,end=" ")