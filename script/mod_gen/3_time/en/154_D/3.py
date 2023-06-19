def dice():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += p[i]
    tmp = ans
    for i in range(K, N):
        tmp += p[i] - p[i-K]
        ans = max(ans, tmp)
    print((ans+K)/2)
dice()
