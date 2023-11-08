# n 입력 00:00:00 ~ N:59:59 까지 3이 하나라도 들어가면 카운트

n = int(input())

count = 0
# 00 : 00 : 00
f = 0
s = 0
t = 0

while(1):
    if(t < 59):
        t += 1
    elif(t == 59):
        t = 0
        if(s < 59):
            s += 1
        elif(s == 59):
            s = 0
            f += 1
            if(f == n + 1):
                break
    tot = str(f) + str(s) + str(t)
    if('3' in tot):
        count += 1

print(count)
