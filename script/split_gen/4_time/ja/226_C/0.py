def main():
    N = int(input())
    T = [0]*(N+1)
    K = [0]*(N+1)
    A = [0]*(N+1)
    for i in range(1,N+1):
        T[i], K[i] = map(int, input().split())
        if K[i] > 0:
            A[i] = list(map(int, input().split()))
    #print(N,T,K,A)
    #dp[i]は技iを習得するのに必要な時間の最小値
    dp = [0]*(N+1)
    for i in range(1,N+1):
        if K[i] == 0:
            dp[i] = T[i]
    #print(dp)
    for i in range(1,N+1):
        if K[i] > 0:
            dp[i] = max(dp[i], T[i])
            for j in range(K[i]):
                dp[i] = max(dp[i], dp[A[i][j]]+T[i])
    #print(dp)
    print(dp[N])
