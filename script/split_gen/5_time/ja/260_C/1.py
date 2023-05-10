def solve():
    N,X,Y = map(int,input().split())
    def f(n):
        if n == 1:
            return 0
        elif n == 2:
            return X
        else:
            return f(n-1) + X + Y*(n-2)
    print(f(N))
