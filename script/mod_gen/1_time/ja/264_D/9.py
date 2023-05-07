def main():
    s = input()
    abc = "atcoder"
    dp = [[0 for j in range(len(abc)+1)] for i in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(abc)+1):
            if s[i-1] == abc[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(len(s) - dp[len(s)][len(abc)])

if __name__ == '__main__':
    main()