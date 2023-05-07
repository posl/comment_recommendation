def solve(H, W, A, B):
    # DP[i][j][k] := i x j のマス目に、
    # 2 x 1 のマットをk枚使って
    # 1 x 1 のマットを残りで塗りつぶす方法の総数
    DP = [[[0] * (A + 1) for _ in range(W + 1)] for _ in range(H + 1)]
    DP[1][1][0] = 1
    for i in range(H + 1):
        for j in range(W + 1):
            for k in range(A + 1):
                if i > 0 and j > 0:
                    DP[i][j][k] += DP[i - 1][j - 1][k]
                if i > 1 and k > 0:
                    DP[i][j][k] += DP[i - 2][j][k - 1]
                if j > 1 and k > 0:
                    DP[i][j][k] += DP[i][j - 2][k - 1]
    return DP[H][W][A]
H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))

if __name__ == '__main__':
    solve()