def readinput():
    h,w=map(int,input().split())
    s=[]
    for _ in range(h):
        s.append(input())
    t=[]
    for _ in range(h):
        t.append(input())
    return h,w,s,t
