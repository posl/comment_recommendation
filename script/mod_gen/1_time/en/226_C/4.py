def main():
    N = int(input())
    T = [0]*N
    K = [0]*N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [float('inf')]*N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i-1]+T[i])
        for a in A[i]:
            dp[i] = min(dp[i], dp[a-1]+T[i])
    print(dp[-1])

if __name__ == '__main__':
    main()