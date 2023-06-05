def solve():
    N,M,T=map(int,input().split())
    A=list(map(int,input().split()))
    XY=[]
    for i in range(M):
        XY.append(list(map(int,input().split())))
    XY.sort()
    t=T
    x=1
    for i in range(M):
        t-=XY[i][0]-x
        if t<=0:
            print("No")
            return
        t+=XY[i][1]
        x=XY[i][0]
    t-=N-x
    if t<=0:
        print("No")
    else:
        print("Yes")
    return

if __name__ == '__main__':
    solve()