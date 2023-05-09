def solve():
    N,X,Y = map(int,input().split())
    print((N-1)*min(X,Y)+1)
