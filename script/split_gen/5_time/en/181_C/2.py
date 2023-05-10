def check(a,b,c):
    if (a[0] == b[0] and a[0] == c[0]) or (a[1] == b[1] and a[1] == c[1]):
        return True
    if (a[1] - b[1]) * (a[0] - c[0]) == (a[0] - b[0]) * (a[1] - c[1]):
        return True
    else:
        return False
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if check(p[i],p[j],p[k]):
                print("Yes")
                exit()
print("No")
