def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    sdp = [0] * (N + 1)
    sdp[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            li = max(1, i - r)
            ri = max(1, i - l + 1)
            dp[i] += sdp[ri] - sdp[li - 1]
        dp[i] %= mod
        sdp[i] = sdp[i - 1] + dp[i]
        sdp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()