def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [False]*(n+1)
    for i in range(n+1):
        for j in range(k):
            if i-a[j]>=0:
                dp[i] = dp[i] or not dp[i-a[j]]
    for i in range(n,-1,-1):
        if dp[i]:
            print(i)
            break

if __name__ == '__main__':
    main()