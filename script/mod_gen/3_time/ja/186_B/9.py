def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # まずは各行の合計値を求める
    sum_row = [0] * H
    for i in range(H):
        sum_row[i] = sum(A[i])
    # 各列の合計値を求める
    sum_col = [0] * W
    for i in range(W):
        for j in range(H):
            sum_col[i] += A[j][i]
    # 各マスのブロックの数を求める
    sum_all = sum(sum_row)
    sum_each = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            sum_each[i][j] = sum_all - sum_row[i] - sum_col[j] + A[i][j]
    # 各マスを全て同じ値にするために必要なブロックの数を求める
    ans = 10 ** 9
    for i in range(H):
        for j in range(W):
            ans = min(ans, sum_each[i][j])
    print(ans)

if __name__ == '__main__':
    solve()