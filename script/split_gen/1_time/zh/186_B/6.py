def readinput():
    H,W=list(map(int,input().split()))
    A=[]
    for i in range(H):
        A.append(list(map(int,input().split())))
    return H,W,A
