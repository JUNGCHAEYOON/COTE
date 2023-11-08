''' 3-1 '''

#거스름돈
#500 100 50 10
#거슬러줄돈 N 은 항상 10배수
#그리디 -> 큰 금액부터 돌려준다.

# 구현
def change(n):
    buff = n
    coin = 0
    # 몫은 더하고
    coin += buff // 500
    # 낮추고
    buff = buff % 500

    coin += buff // 100
    buff = buff % 100

    coin += buff//50
    buff = buff % 50

    coin += buff//10
    return coin

# main
n = 1260
print(change(n))

# 답안지
n = 1260
count = 0

list = [500, 100, 50, 10]
for coin in list:
    count += n // coin
    n %= coin

print(count)