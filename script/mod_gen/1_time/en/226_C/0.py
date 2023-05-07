def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if K[i] == 0:
            dp[i] = T[i]
        else:
            dp[i] = max(T[i] + dp[j] for j in A[i])
    print(dp[0])

if __name__ == '__main__':
    main()