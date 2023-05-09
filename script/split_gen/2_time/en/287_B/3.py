def readinput():
    n,m=input().split()
    n=int(n)
    m=int(m)
    s=[]
    for _ in range(n):
        s.append(input())
    t=[]
    for _ in range(m):
        t.append(input())
    return n,m,s,t
