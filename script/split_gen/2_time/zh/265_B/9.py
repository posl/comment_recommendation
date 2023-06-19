def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    i = 0
    for x,y in XY:
        while i < N-1 and i+1 < x:
            T -= A[i]
            if T <= 0:
                print("No")
                return
            i += 1
        T += y
        if T > A[i]:
            T = A[i]
        i += 1
    while i < N-1:
        T -= A[i]
        if T <= 0:
            print("No")
            return
        i += 1
    print("Yes")
