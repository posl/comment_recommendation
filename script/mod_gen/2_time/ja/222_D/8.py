def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    # C[i][j] = (i,j)の範囲のCの個数
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        C[i][i] = 1
    # 逆順に埋めていく
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N + 1):
            # C[i][j] = C[i][k] * C[k][j]の和
            for k in range(i, j):
                C[i][j] += C[i][k] * C[k][j]
            # A[i] <= C[i][j] <= B[i]になるように調整
            C[i][j] -= C[i][j] - A[i] - B[i]
            C[i][j] %= 998244353
    print(C[0][N])

if __name__ == '__main__':
    main()