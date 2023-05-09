def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i - A[j]] == 0:
                    dp[i] = 1
                    break
    print(dp[N])

if __name__ == '__main__':
    main()