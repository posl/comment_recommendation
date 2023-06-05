def main():
    S = input()
    if S == '0':
        print(0)
        return
    ans = 10000000
    for i in range(1, 11):
        if i == 1:
            dp = [0] * len(S)
            if S[0] != '1':
                dp[0] = 1
        else:
            dp = [10000000] * len(S)
            if S[0] != '1':
                dp[0] = 2
            else:
                dp[0] = 1
        for j in range(1, len(S)):
            if S[j] == '0':
                dp[j] = dp[j - 1] + 1
            else:
                if dp[j - 1] == 10000000:
                    dp[j] = 10000000
                else:
                    dp[j] = min(dp[j], dp[j - 1] + i)
            if j == len(S) - 1:
                if S[j] == '1':
                    ans = min(ans, dp[j])
                else:
                    ans = min(ans, dp[j] + 1)
    print(ans)

if __name__ == '__main__':
    main()