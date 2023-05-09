def main():
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*(1<<N) for _ in range(N+1)]
    for i in range(N-1,-1,-1):
        for j in range(1<<N):
            if bin(j).count('1') == i:
                for k in range(N):
                    if j>>k&1:
                        dp[i][j] = max(dp[i][j], dp[i+1][j^(1<<k)]+A[i][k])
    print(dp[0][-1])
