def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        if a[i] == a[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    print(n-dp[-1])

if __name__ == '__main__':
    main()