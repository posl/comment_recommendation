def  main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp = [0] * N
    dp[0] = 1
    sumdp = [0] * (N + 1)
    sumdp[1] = 1
    for i in range(N):
        for l, r in LR:
            dp[i] += sumdp[max(0, i - l + 1)] - sumdp[max(0, i - r)]
        dp[i] %= 998244353
        sumdp[i + 1] = sumdp[i] + dp[i]
    print(dp[-1])

if __name__ == '__main__':
    ()