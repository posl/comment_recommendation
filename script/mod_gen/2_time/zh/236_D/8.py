def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for i in range(1 << N)] for j in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(1 << N):
            for k in range(N):
                if j >> k & 1:
                    continue
                for l in range(k + 1, N):
                    if j >> l & 1:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i + 1][j | (1 << k) | (1 << l)] + A[k][l])
    print(dp[0][0])

if __name__ == '__main__':
    main()