def readinput():
    n,m,t=list(map(int,input().split()))
    ab=[]
    for i in range(m):
        ab.append(list(map(int,input().split())))
    return n,m,t,ab
