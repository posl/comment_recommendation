def main():
    N = int(input())
    #T,X,A = [list(map(int,input().split())) for _ in range(N)]
    T = [0]*(N+1)
    X = [0]*(N+1)
    A = [0]*(N+1)
    for i in range(N):
        T[i+1],X[i+1],A[i+1] = map(int,input().split())
    #print(N,T,X,A)
    #dp[i][j] = i番目までのスヌーケを捕まえたときの、最大のスコア
    dp = [[0]*5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            #i番目のスヌーケを捕まえない場合
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            #i番目のスヌーケを捕まえる場合
            if T[i+1] - T[i] >= abs(X[i+1] - j):
                dp[i+1][X[i+1]] = max(dp[i+1][X[i+1]],dp[i][j] + A[i+1])
    #print(dp)
    print(max(dp[N]))

if __name__ == '__main__':
    main()