def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #print(T)
    #print(X)
    #print(A)
    #dp = [0] * (T[N-1] + 1)
    dp = [0] * 5
    for i in range(N):
        #print(i)
        #print(dp)
        #print(dp[T[i]])
        #print(dp[X[i]])
        #print(dp[X[i]] + A[i])
        if dp[X[i]] < dp[T[i]]:
            dp[X[i]] = dp[T[i]]
        if dp[T[i]] + A[i] > dp[X[i]]:
            dp[X[i]] = dp[T[i]] + A[i]
    print(dp[4])
    return
solve()
