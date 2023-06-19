def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0] * n
    for i in range(n):
        for j in range(k[i]):
            dp[a[i][j]-1] = max(dp[a[i][j]-1], dp[i] + t[i])
    print(max(dp) + t[-1])

if __name__ == '__main__':
    main()