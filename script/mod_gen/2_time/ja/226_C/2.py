def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * N
    for i in range(N):
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j] - 1])
        dp[i] += T[i]
    print(dp[-1])

if __name__ == '__main__':
    main()