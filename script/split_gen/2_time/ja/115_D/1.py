def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return burger(n-1,x-1)
    else:
        return p[n-1] + 1 + burger(n-1,x-2-a[n-1])
n,x = map(int,input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(a[i]*2+3)
    p.append(p[i]*2+1)
print(burger(n,x))
