def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    for x,y in XY:
        A.insert(x-1,y)
    for i in range(N-1):
        T -= A[i]
        if T <= 0:
            return False
    return True
