def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for _ in range(h):
        si=input()
        s.append(si)
    return h,w,s
