def main():
    #input
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_temp, k_temp, *a_temp = map(int, input().split())
        t.append(t_temp)
        k.append(k_temp)
        a.append(a_temp)
    #init
    dp = [0 for i in range(n+1)]
    #dp
    for i in range(n):
        dp[a[i][0]] = max(dp[a[i][0]], dp[i+1] + t[i])
        for j in range(1, k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i+1])
    #output
    print(dp[n])

if __name__ == '__main__':
    main()