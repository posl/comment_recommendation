def main():
    n, x = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    a_b.sort(key=lambda x: x[0])
    #print(a_b)
    dp = [[False]*(x+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j + a_b[i][0] <= x:
                    dp[i+1][j+a_b[i][0]] = True
    if dp[n][x]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()