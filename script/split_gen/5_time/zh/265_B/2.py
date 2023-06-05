def get_input():
    n,m,t=map(int,input().split())
    a=list(map(int,input().split()))
    xy=[list(map(int,input().split())) for _ in range(m)]
    return n,m,t,a,xy
