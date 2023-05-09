def readinput():
    n,m,q=map(int,input().split())
    lr=[]
    for _ in range(m):
        l,r=map(int,input().split())
        lr.append((l,r))
    pq=[]
    for _ in range(q):
        p,q=map(int,input().split())
        pq.append((p,q))
    return n,m,q,lr,pq
