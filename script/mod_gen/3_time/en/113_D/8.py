def main():
    h, w, k = map(int, input().split())
    dp = [0] * w
    dp[0] = 1
    for _ in range(h):
        new_dp = [0] * w
        for i in range(w):
            if i == 0:
                new_dp[i] += dp[i] + dp[i + 1]
            elif i == w - 1:
                new_dp[i] += dp[i] + dp[i - 1]
            else:
                new_dp[i] += dp[i] + dp[i - 1] + dp[i + 1]
        dp = new_dp
    print(dp[k - 1] % 10 ** 9 + 7)

if __name__ == '__main__':
    main()