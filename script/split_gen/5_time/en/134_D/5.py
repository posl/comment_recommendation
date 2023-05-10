def check(a):
    n = len(a)
    for i in range(1,n+1):
        s = 0
        for j in range(1,n+1):
            if j%i == 0:
                s += a[j-1]
        if s%2 != a[i-1]:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n):
    if check(b + [0]) and check(b + [1]):
        b.append(0)
    else:
        b.append(1)
print(sum(b))
for i in range(n):
    if b[i] == 1:
        print(i+1)
