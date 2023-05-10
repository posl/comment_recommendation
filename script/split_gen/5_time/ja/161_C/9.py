def solve():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, K - ans)
    print(ans)
