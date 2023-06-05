def min_step(r,x,y):
    if x**2 + y**2 < r**2:
        return 2
    else:
        return int((x**2 + y**2)**0.5/r) + 1
r,x,y = map(int,input().split())
print(min_step(r,x,y))
