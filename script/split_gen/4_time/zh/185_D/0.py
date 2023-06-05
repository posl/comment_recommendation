def input():
    n,m = map(int,input().split())
    if m == 0:
        return 1
    a = list(map(int,input().split()))
    return n,m,a
