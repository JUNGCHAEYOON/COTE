import sys

# 배열의 크기 n
# 숫자가 더해지는 횟수 m
# 연속가능한수 k

# 가장큰수 max를 찾기
# 두번째로 큰수 submax 찾기
# answer = 0 에서 k만큼 for문 max 더하기
# submax 더하기
# 다시 for 문 max 더하기
# 총 for문 m

#__main
n,m,k = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

data.sort()
maxi = data[n-1]
submax = data[n-2]

total = 0
buffk = k
for i in range(m):
    if(buffk != 0):
        total += maxi
        buffk -= 1
    elif(buffk == 0):
        total += submax
        buffk = k

print(total)

# 해답
n,m,k = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while(1):
    for i in range(k):
        if (m == 0):
            break
        result += first
        m -= 1
    if (m == 0):
        break
    result += second
    m -= 1

print(result)