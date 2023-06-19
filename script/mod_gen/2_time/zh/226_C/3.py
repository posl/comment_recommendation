def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_i, k_i, *a_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
        a.append(a_i)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + t[i])
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i])
    print(dp[n])

if __name__ == '__main__':
    main()