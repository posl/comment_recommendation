def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            return 'No'
        for x, y in XY:
            if i+1 == x:
                time += y
                break
    return 'Yes'
