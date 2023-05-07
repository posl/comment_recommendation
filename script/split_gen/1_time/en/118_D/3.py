def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for a in A:
            if i-a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a]+1)
    ans = ""
    while N > 0:
        for a in A:
            if N-a >= 0 and dp[N-a] == dp[N]-1:
                ans += str(a)
                N -= a
                break
    print(ans)
