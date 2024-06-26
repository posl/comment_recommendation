def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print(dp[-1][-1])

if __name__ == '__main__':
    main()