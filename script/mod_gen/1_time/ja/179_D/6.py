def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    dp[0] = 1
    s = [0] * (N + 1)
    s[0] = 1
    for i in range(N):
        for l, r in LR:
            if i + l > N:
                break
            dp[i + l] += s[i] - s[max(0, i - r - 1)]
            dp[i + l] %= 998244353
        s[i + 1] = (s[i] + dp[i + 1]) % 998244353
    print(dp[N])

if __name__ == '__main__':
    main()