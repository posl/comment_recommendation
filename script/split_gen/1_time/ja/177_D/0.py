def readinput():
    n,m=map(int,input().split())
    ab=[]
    for _ in range(m):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,m,ab
