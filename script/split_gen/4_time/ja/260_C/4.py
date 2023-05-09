def solve():
    n,x,y = map(int,input().split())
    if x >= y:
        print((n-1)*y)
    else:
        print((n-1)*x)
