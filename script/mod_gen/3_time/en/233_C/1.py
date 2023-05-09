def solve():
    N,X = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int,input().split()))
        L.append(l[0])
        A.append(l[1:])
    
    #dp[i][j] = i番目までのバッグの中から選んだj個の積がXの倍数であるような選び方の個数
    dp = [[0 for i in range(10**5+1)] for j in range(N)]
    for i in range(N):
        for j in range(L[i]):
            if A[i][j] == X:
                dp[i][1] += 1
            elif X%A[i][j] == 0:
                dp[i][0] += 1
    for i in range(1,N):
        for j in range(10**5+1):
            for k in range(L[i]):
                if j == 0:
                    if X%A[i][k] == 0:
                        dp[i][j] += dp[i-1][j]
                else:
                    if A[i][k] == X:
                        dp[i][j] += dp[i-1][j-1]
                    elif X%A[i][k] == 0:
                        dp[i][j] += dp[i-1][j-1]
    print(dp[N-1][0]+dp[N-1][1]+dp[N-1][2])
solve()

if __name__ == '__main__':
    solve()