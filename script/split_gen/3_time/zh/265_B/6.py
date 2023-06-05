def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = []
    for i in range(M):
        XY.append(list(map(int,input().split())))
    #print(N,M,T,A,XY)
    now = 0
    for i in range(N-1):
        now += A[i]
        for j in range(M):
            if XY[j][0] == i+2:
                now += XY[j][1]
        if now >= T:
            print("No")
            return
    print("Yes")
