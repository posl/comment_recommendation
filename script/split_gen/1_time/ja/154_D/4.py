def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0.0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K])/K)
    print(ans)
    return 0
