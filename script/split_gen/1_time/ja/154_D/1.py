def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0.0
    for i in range(K):
        ans += (P[i] + 1) / 2
    tmp = ans
    for i in range(N - K):
        tmp += (P[i + K] + 1) / 2 - (P[i] + 1) / 2
        ans = max(ans, tmp)
    print(ans)
    return 0
