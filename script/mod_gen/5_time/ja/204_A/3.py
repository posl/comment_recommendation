def f(x,y):
    if x==y:
        return x
    elif x!=0 and y!=0:
        return 0
    elif x!=1 and y!=1:
        return 1
    else:
        return 2
x,y=map(int,input().split())
print(f(x,y))
