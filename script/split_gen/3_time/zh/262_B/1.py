def readinput():
    n,m=map(int,input().split())
    uv=[]
    for _ in range(m):
        u,v=map(int,input().split())
        uv.append((u,v))
    return n,m,uv
