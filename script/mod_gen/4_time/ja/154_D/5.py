def solve(N, K, p):
    s = 0
    for i in range(K):
        s += p[i]
    m = s
    for i in range(K, N):
        s -= p[i-K]
        s += p[i]
        m = max(m, s)
    return (m + K) / 2
N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))
