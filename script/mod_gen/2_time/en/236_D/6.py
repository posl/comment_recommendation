def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for _ in range(2 ** N)] for _ in range(N)]
    for i in range(N):
        for j in range(2 ** N):
            for k in range(N):
                if (j & (1 << k)) == 0:
                    dp[i][j | (1 << k)] = max(dp[i][j | (1 << k)], dp[i][j] ^ A[i][k])
    dp2 = [0 for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(N):
            if (i & (1 << j)) == 0:
                dp2[i | (1 << j)] = max(dp2[i | (1 << j)], dp[j][i])
    print(dp2[2 ** N - 1])

if __name__ == '__main__':
    main()