def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a > N:
                continue
            dp[i+a] = max(dp[i+a],dp[i]+1)
    ans = ''
    for i in range(dp[N]):
        for a in A:
            if N - a < 0:
                continue
            if dp[N-a] == dp[N] - i - 1:
                ans += str(a)
                N -= a
                break
    print(ans)
