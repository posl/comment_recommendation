def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    A = sorted(A, reverse=True)
    #print(A)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(M):
            if i - match[A[j]-1] >= 0:
                dp[i] = max(dp[i], dp[i-match[A[j]-1]]*10+A[j])
    #print(dp)
    print(dp[N])

if __name__ == '__main__':
    main()