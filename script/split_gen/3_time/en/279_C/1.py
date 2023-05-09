def readinput():
    h,w=readArray(int)
    s=[]
    for _ in range(h):
        s.append(input())
    t=[]
    for _ in range(h):
        t.append(input())
    return h,w,s,t
