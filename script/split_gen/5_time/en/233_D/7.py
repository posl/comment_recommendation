def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(N):
        s += A[r]
        while s >= K:
            if s == K:
                ans += 1
            s -= A[l]
            l += 1
    print(ans)
