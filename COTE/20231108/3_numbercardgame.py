import sys

# 각행마다 가장 작은 수를 구해서 리스트에 넣은뒤 그중 가장큰것 뽑으면 댐
# n,m = map(int, sys.stdin.readline().split())
#
# data = []
# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))
#
# small = []
# for e in data:
#     small.append(min(e))
#
# print(max(small))


# 해답
n,m = map(int, sys.stdin.readline().split())
result = 0

for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)