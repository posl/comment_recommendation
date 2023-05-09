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
    #dp = [[0] * 5 for i in range(N+1)]
    #dp[0][0] = 0
    #dp[0][1] = 0
    #dp[0][2] = 0
    #dp[0][3] = 0
    #dp[0][4] = 0
    dp = [0] * 5
    for i in range(N):
        #for j in range(5):
        #    dp[i+1][j] = dp[i][j]
        dp2 = [0] * 5
        for j in range(5):
            dp2[j] = dp[j]
        #print(dp2)
        for j in range(5):
            #if dp[i+1][j] < dp[i][j]:
            #    dp[i+1][j] = dp[i][j]
            if dp2[j] < dp[j]:
                dp2[j] = dp[j]
            if j == X[i]:
                #if dp[i+1][j] < dp[i][j] + A[i]:
                #    dp[i+1][j] = dp[i][j] + A[i]
                if dp2[j] < dp[j] + A[i]:
                    dp2[j] = dp[j] + A[i]
            #if dp[i+1][j] < dp[i][j] + A[i]:
            #    dp[i+1][j] = dp[i][j] + A[i]
            if j > 0:
                #if dp[i+1][j-1] < dp[i][j]:
                #    dp[i+1][j-1] = dp[i][j]
                if dp2[j-1] < dp[j]:
                    dp2[j-1] = dp[j]
        #print(dp2)
        #dp = dp2
        for j in range(5):
            dp[j] = dp2[j]
        #

if __name__ == '__main__':
    solve()