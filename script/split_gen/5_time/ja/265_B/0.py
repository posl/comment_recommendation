def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if i+1 in [x for x,y in XY]:
            t += [y for x,y in XY if x == i+1][0]
            if t > T:
                t = T
    print("Yes")
    return
