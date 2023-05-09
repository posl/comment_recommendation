def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            v = V[:i] + V[N - j:]
            v.sort()
            ans = max(ans, sum(v[max(0, i + j - K):]))
    print(ans)
