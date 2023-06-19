def f1():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.append(t)
    b.append(t)
    l = 0
    for i in range(m+1):
        l += (b[i]-a[i])
    if l >= n:
        print("Yes")
    else:
        print("No")
