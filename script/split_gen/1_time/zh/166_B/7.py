def readinput():
    n,k=list(map(int,input().split()))
    d=[]
    a=[]
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int,input().split())))
    return n,k,d,a
