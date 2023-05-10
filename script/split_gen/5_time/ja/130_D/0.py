def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    t = 0
    r = 0
    for l in range(N):
        while r < N and t < K:
            t += A[r]
            r += 1
        if t < K:
            break
        ans += N - r + 1
        t -= A[l]
    print(ans)
solve()
