def main():
    N, K = map(int, input().split())
    seg = []
    for _ in range(K):
        L, R = map(int, input().split())
        seg.append((L, R))
    dp = [0] * (N + 1)
    dp[1] = 1
    sdp = [0] * (N + 1)
    sdp[1] = 1
    for i in range(2, N + 1):
        for L, R in seg:
            if i - L < 0:
                continue
            dp[i] += sdp[i - L] - sdp[max(0, i - R - 1)]
        dp[i] %= 998244353
        sdp[i] = (sdp[i - 1] + dp[i]) % 998244353
    print(dp[N])

if __name__ == '__main__':
    main()