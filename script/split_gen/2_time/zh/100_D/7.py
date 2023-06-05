def max_abs_sum(x,y,z):
    a = []
    for i in range(len(x)):
        a.append(x[i]+y[i]+z[i])
    a.sort()
    return a[0]+a[1]+a[2]
n,m = map(int,input().split())
x = []
y = []
z = []
for i in range(n):
    x1,y1,z1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
    z.append(z1)
