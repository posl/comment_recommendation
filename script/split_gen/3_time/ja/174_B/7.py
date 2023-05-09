def get_input():
    n,d = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(n)]
    return n,d,xy
