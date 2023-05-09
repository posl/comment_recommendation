def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(N):
        p[i] = (p[i] + 1) / 2
    s = sum(p[:K])
    ans = s
    for i in range(N - K):
        s += p[i + K] - p[i]
        ans = max(ans, s)
    print(ans)
