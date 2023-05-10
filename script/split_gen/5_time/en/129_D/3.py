def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for _ in range(h):
        s.append(input())
    return h,w,s
