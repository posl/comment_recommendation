def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = [[0 for j in range(3001)] for i in range(N)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = sum(dp[i-1][A[i-1]:j+1]) % 998244353
    print(sum(dp[N-1]) % 998244353)
