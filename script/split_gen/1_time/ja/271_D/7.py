def main():
    N, S = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i][0]:
                dp[i + 1][j] = dp[i][j - A[i][0]] or dp[i][j]
            if j >= A[i][1]:
                dp[i + 1][j] = dp[i][j - A[i][1]] or dp[i][j]
    if dp[N][S]:
        print('Yes')
        T = ['H' if dp[i][S - A[i][0]] else 'T' for i in range(N)]
        print(''.join(T))
    else:
        print('No')
