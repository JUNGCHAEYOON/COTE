#       a b c d e f g h
#
# 1     2 3 4 4 4 4 3 2
# 2     3 4 6 6 6 6 4 3
# 3     4 6 8 8 8 8 6 4
# 4
# 5
# 6
# 7
# 8

# 한쪽 방향에 대해서 +2 까지 가능하다
n = input()

# 아스키코드 a = 97, A = 65
x = ord(n[0]) - 96
y = int(n[1])

steps = [(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]

count = 0
for step in steps:
    if(x + step[0] >= 1 and y + step[1] >= 1 and x + step[0] <= 8 and y + step[1] <= 8):
        count += 1

print(count)