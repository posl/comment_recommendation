def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, m, a)
    l = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    a = [l[i-1] for i in a]
    #print(a)
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(m):
            if i >= a[j]:
                dp[i] = max(dp[i], dp[i-a[j]]*10+j+1)
    print(dp[n])

if __name__ == '__main__':
    main()