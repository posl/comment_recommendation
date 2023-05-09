def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    sumA = sum(A)
    dp = [0] * (sumA + 1)
    dp[0] = 1
    for a in A:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == 0:
                continue
            dp[i + a] += dp[i]
            dp[i + a] %= mod
    ans = 0
    for i in range(len(dp)):
        if dp[i] == 0:
            continue
        if i % N != 0:
            continue
        ans += dp[i]
        ans %= mod
    print(ans)
