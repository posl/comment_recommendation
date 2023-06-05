def f(x):
    return ((x-sx)*(gy-sy)/(gx-sx)+sy)
sx,sy,gx,gy=map(int,input().split())
print(f(gx))
