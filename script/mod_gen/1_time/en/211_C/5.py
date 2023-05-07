def main():
    S = input()
    N = len(S)
    MOD = 10**9+7
    dp = [0]*8
    dp[0] = 1
    for s in S:
        for i in range(8):
            if s == "chokudai"[i]:
                dp[i+1] += dp[i]
                dp[i+1] %= MOD
    print(dp[-1])

if __name__ == '__main__':
    main()