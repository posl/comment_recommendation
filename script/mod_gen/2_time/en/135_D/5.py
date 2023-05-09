def main():
    S = input()
    dp = [0] * 13
    dp[0] = 1
    for s in S:
        if s == '?':
            new_dp = [0] * 13
            for i in range(10):
                for j in range(13):
                    new_dp[(j * 10 + i) % 13] += dp[j]
            dp = new_dp
        else:
            new_dp = [0] * 13
            for j in range(13):
                new_dp[(j * 10 + int(s)) % 13] += dp[j]
            dp = new_dp
        dp = [i % (10**9 + 7) for i in dp]
    print(dp[5])

if __name__ == '__main__':
    main()