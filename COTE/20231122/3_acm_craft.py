import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    d = list(map(int,sys.stdin.readline().split()))
    array = []
    for i in range(k):
        x,y = map(int,sys.stdin.readline().split())
        array.append([x,y])
    w = int(sys.stdin.readline())

    # solution
    # array 를 돌면서 시작노드부터 w 까지 가는 경우의수를 찾는다.
    # 해당 경우의수를 temp에 담는다
    # temp[0] 이 1,3,4 인경우 d1 + d3 + d4 이런식으로 합산한다
    # max(temp) 를 리턴한다.

# array = [[1,2],[1,3],[2,4],[3,4]]
