def readinput():
    n=int(input())
    xyplist=[]
    for i in range(n):
        xyplist.append(list(map(int,input().split())))
    return n,xyplist
