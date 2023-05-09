def readinput():
    n,m,x=map(int,input().split())
    c=[]
    a=[]
    for _ in range(n):
        line=list(map(int,input().split()))
        c.append(line[0])
        a.append(line[1:])
    return n,m,x,c,a
