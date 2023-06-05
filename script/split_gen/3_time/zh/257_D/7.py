def readinput():
    n=int(input())
    xyplist=[]
    for _ in range(n):
        x,y,p=map(int,input().split())
        xyplist.append((x,y,p))
    return n,xyplist
