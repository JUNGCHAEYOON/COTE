n,m = map(int,input().split())

# n x m 맵 생성 0으로 채움
d = [[0] * m for _ in range(n)]

x,y,direction = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문했으므로 1로 처리

# 맵 생성
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 북동서남
dx = [-1,0,1,0]
dy = [0,1,-1,0]

def turn_left():
    global direction
    direction -= 1
    if(direction == -1) :
        direction = 3

count = 1
turn_time = 0
while (1):
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    # 회전 후 가보지 않은 칸 존재
    if(d[nx][ny] == 0 and array[nx][ny] == 0):
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전후 가보지않은 칸이 없거나 바다
    else:
        turn_time += 1
    if(turn_time == 4):
        nx = x - dx[direction]
        ny = y - dy[direction]
        if(array[nx][ny] == 0):
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

