def solve():
    R, X, Y = map(int, input().split())
    if (X*X+Y*Y)%(R*R)!=0:
        print((X*X+Y*Y)//(R*R)+1)
    else:
        print((X*X+Y*Y)//(R*R))
solve()
