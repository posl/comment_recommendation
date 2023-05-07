def main():
    N = int(input())
    T_X_A = [list(map(int, input().split())) for _ in range(N)]
    #print(T_X_A)
    #print(N)
    dp = [[0]*5 for _ in range(10**5+1)]
    for i in range(N):
        for j in range(5):
            if T_X_A[i][1] == j:
                dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][j] + T_X_A[i][2])
            else:
                dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][j])
            dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][T_X_A[i][1]])
    
    #print(dp)
    print(max(dp[N]))
