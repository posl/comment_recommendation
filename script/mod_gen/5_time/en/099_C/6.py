def main():
    n = int(input())
    dp = [i for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i):
            if j**6 > i:
                break
            dp[i] = min(dp[i], dp[i-j**6]+1)
        for j in range(1,i):
            if j**9 > i:
                break
            dp[i] = min(dp[i], dp[i-j**9]+1)
    print(dp[n])

if __name__ == '__main__':
    main()