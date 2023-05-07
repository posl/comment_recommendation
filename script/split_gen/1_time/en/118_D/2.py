def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1 for _ in range(N+1)]
    dp[0] = 0
    for i in range(1, N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a] + 1)
    ans = []
    n = N
    while n > 0:
        for a in A:
            if n - a >= 0 and dp[n-a] == dp[n] - 1:
                ans.append(a)
                n -= a
                break
    print(''.join(map(str, ans)))
