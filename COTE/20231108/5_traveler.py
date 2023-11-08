import sys

n = int(sys.stdin.readline())
plans = input().split()

player = [1,1]

for plan in plans:
    if(plan == 'R'):
        if(player[1] < n + 1):
            player[1] += 1
    elif(plan == 'L'):
        if(player[1] > 1):
            player[1] -= 1
    elif(plan == 'U'):
        if(player[0] > 1):
            player[0] -= 1
    elif(plan == "D"):
        if(player[0] < n + 1):
            player[0] += 1

print(player[0], player[1])