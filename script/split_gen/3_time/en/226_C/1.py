def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    #print(N)
    #print(T)
    #print(K)
    #print(A)
    #print("end of input")
    #print("")
    #dp[i] = minimum time to learn move i
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = dp[i] + T[i]
        for j in range(K[i]):
            dp[i+1] = min(dp[i+1], dp[A[i][j]-1] + T[i])
    #print(dp)
    print(dp[N])
