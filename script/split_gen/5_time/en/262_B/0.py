def readinput():
    n,m=list(map(int,input().split()))
    u=[]
    v=[]
    for _ in range(m):
        ui,vi=list(map(int,input().split()))
        u.append(ui)
        v.append(vi)
    return n,m,u,v
