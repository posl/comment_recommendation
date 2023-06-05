def main():
    S = input()
    chokudai = "chokudai"
    #dp = [0] * 9
    dp = [0 for _ in range(9)]
    dp[0] = 1
    mod = 10**9 + 7
    for i in range(len(S)):
        for j in range(8):
            if S[i] == chokudai[j]:
                dp[j+1] += dp[j]
                dp[j+1] %= mod
    print(dp[8])

if __name__ == '__main__':
    main()