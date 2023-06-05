def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0] * (1 << N) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            dp[i][1 << j] = A[i][j]
    for i in range(1, 1 << N):
        for j in range(N):
            if not (i & (1 << j)):
                continue
            for k in range(N):
                if i & (1 << k):
                    continue
                dp[k][i | (1 << k)] = max(dp[k][i | (1 << k)], dp[j][i] + A[k][j])
    print(dp[N - 1][(1 << N) - 1])
main()
