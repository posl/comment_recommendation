def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0] * n
    sdp = [0] * (n+1)
    dp[0] = 1
    sdp[1] = 1
    for i in range(1, n):
        for l, r in lr:
            if i - l < 0:
                break
            dp[i] += sdp[i-l+1] - sdp[max(i-r, 0)] + mod
            dp[i] %= mod
        sdp[i+1] = sdp[i] + dp[i]
        sdp[i+1] %= mod
    print(dp[-1])
main()

if __name__ == '__main__':
    main()