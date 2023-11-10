n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

def change():
    global a
    global b
    a = sorted(a)
    b = sorted(b,reverse=True)
    for i in range(k):
        for j in range(len(a)):
            if(a[j] < b[j]):
                a[j],b[j] = b[j],a[j]
            else:
                break
change()
print(a)
print(b)
