def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (N+1)
    for i in range(N+1):
        for j in range(K):
            if i >= A[j] and dp[i-A[j]] == False:
                dp[i] = True
                break
    print(dp.count(False))

if __name__ == '__main__':
    main()