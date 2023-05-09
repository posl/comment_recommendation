def main():
    N = int(input())
    T = [0]
    K = [0]
    A = [[]]
    for i in range(N):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(list(map(int, input().split())))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + T[i]
        for j in A[i]:
            dp[i] = min(dp[i], dp[j] + T[i])
    print(dp[N])

if __name__ == '__main__':
    main()