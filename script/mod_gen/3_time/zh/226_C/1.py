def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        tmp = input().split()
        T.append(int(tmp[0]))
        K.append(int(tmp[1]))
        A.append(list(map(lambda x:int(x)-1, tmp[2:])))
    #print(T)
    #print(K)
    #print(A)
    #print('=====================')
    T = [0] + T
    K = [0] + K
    A = [[]] + A
    #print(T)
    #print(K)
    #print(A)
    #print('=====================')
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j]+1] + T[A[i][j]+1])
    #print(dp)
    print(dp[N] + T[N])

if __name__ == '__main__':
    main()