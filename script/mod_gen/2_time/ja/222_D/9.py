def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # DP[i][j] = (i番目まで見て、j以下の数が何個あるか)
    DP = [[0] * (N + 1) for _ in range(N + 1)]
    DP[0][0] = 1
    for i in range(N):
        for j in range(N):
            DP[i + 1][j] += DP[i][j]
            DP[i + 1][j] %= 998244353
            if A[i] <= j <= B[i]:
                DP[i + 1][j + 1] += DP[i][j]
                DP[i + 1][j + 1] %= 998244353
    print(DP[N][N])

if __name__ == '__main__':
    main()