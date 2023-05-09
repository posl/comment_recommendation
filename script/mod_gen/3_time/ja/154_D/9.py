def solve(N, K, p):
    p = [1 + x for x in p]
    s = sum(p[:K])
    m = s
    for i in range(N - K):
        s = s - p[i] + p[i + K]
        m = max(m, s)
    return m / 2
N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))

if __name__ == '__main__':
    solve()