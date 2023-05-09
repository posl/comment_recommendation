def readinput():
    n=int(input())
    t=[]
    k=[]
    a=[]
    for _ in range(n):
        line=input()
        t1,k1,a1=map(int,line.split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    return n,t,k,a
