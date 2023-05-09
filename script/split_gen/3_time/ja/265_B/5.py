def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    cur = T
    for i in range(N-1):
        cur -= A[i]
        if cur <= 0:
            print('No')
            exit()
        cur += A[i]
        for x, y in XY:
            if i+1 == x:
                cur = min(cur + y, T)
    print('Yes')
