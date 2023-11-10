n = int(input())

array = []
for i in range(n):
    _input = input().split()
    array.append((_input[0],int(_input[1])))

array = sorted(array,key=lambda student : student[1])
# array 의 element 를 student 로 지정
# student[0] 이름 student[1] 점수
# key=lambda student : student[1]

for student in array:
    print(student[0], end=" ")