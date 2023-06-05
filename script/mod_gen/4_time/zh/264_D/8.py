def main():
    S = input()
    atcoder = 'atcoder'
    n = len(S)
    dp = [[0 for _ in range(n+1)] for _ in range(8+1)]
    for i in range(1, n+1):
        for j in range(1, 8+1):
            if S[i-1] == atcoder[j-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = dp[j][i-1]
    print(n - max(dp[8]))

if __name__ == '__main__':
    main()