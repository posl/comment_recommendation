def main():
    N = int(input())
    T = [0]
    X = [0]
    A = [0]
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    #print(T)
    #print(X)
    #print(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if X[i] == 0:
            dp[i] = dp[i-1] + A[i]
        else:
            dp[i] = max(dp[i-1], dp[i-X[i]] + A[i])
    print(dp[N])

if __name__ == '__main__':
    main()