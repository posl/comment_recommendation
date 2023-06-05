def is_convex():
    x = []
    y = []
    for i in range(4):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    x.append(x[0])
    y.append(y[0])
    a = 0
    for i in range(4):
        if (x[i+1]-x[i])*(y[i+2]-y[i+1])-(x[i+2]-x[i+1])*(y[i+1]-y[i]) > 0:
            a+=1
        elif (x[i+1]-x[i])*(y[i+2]-y[i+1])-(x[i+2]-x[i+1])*(y[i+1]-y[i]) < 0:
            a-=1
    if a == 4 or a == -4:
        print("Yes")
    else:
        print("No")
is_convex()
