def f(n,k,a):
    m = k//n
    b = [m for i in range(n)]
    c = [i for i in range(n)]
    d = list(zip(a,b,c))
    d.sort()
    for i in range(k%n):
        d[i] = (d[i][0],d[i][1]+1,d[i][2])
    d.sort(key=lambda x:x[2])
    for i in range(n):
        print(d[i][1])
n,k = map(int,input().split())
a = list(map(int,input().split()))
f(n,k,a)
