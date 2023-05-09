def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))
    
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[0][0] = 1
    
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if c[i][j] == '#':
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[h-1][w-1] % (10**9 + 7))

if __name__ == '__main__':
    main()