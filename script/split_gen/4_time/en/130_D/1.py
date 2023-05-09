def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    r = 0
    ans = 0
    for l in range(N):
        while r < N and s < K:
            s += a[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        s -= a[l]
    print(ans)
