def main():
    N, A, B = map(int, input().split())
    S = input()
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = dp[i] + A
        for j in range(i):
            if S[i-j-1] != S[i]:
                continue
            dp[i+1] = min(dp[i+1], dp[i-j-1]+B)
    print(dp[N])
