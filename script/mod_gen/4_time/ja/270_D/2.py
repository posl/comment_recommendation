def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(k):
            if i-a[j] >= 0:
                if dp[i-a[j]] == 0:
                    dp[i] = 1
    print(dp)
    if dp[n] == 1:
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    main()