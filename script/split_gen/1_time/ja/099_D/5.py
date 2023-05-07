def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 前処理
    # 1. 3 で割った余りごとに色を分ける
    # 2. 各色のマスの個数を数える
    # 3. 各色のマスの個数から、各色のマスに塗り替えるときの違和感を求める
    # 4. 3 つの色の違和感の和が最小になるように塗り替える
    # 5. 1 から 4 までを 3 で割った余りごとに繰り返す
    # 6. 5 つの値の和が答え
    # 1. 3 で割った余りごとに色を分ける
    c1 = [[0] * C for _ in range(3)]
    c2 = [[0] * C for _ in range(3)]
    c3 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                c1[c[i][j] - 1][0] += 1
            elif (i + j) % 3 == 1:
                c2[c[i][j] - 1][1] += 1
            else:
                c3[c[i][j] - 1][2] += 1
    # 2. 各色のマスの個数を数える
    for i in range(C):
        for j in range(3):
            c1[i][j] += c1[i][j - 1]
            c2[i][j] += c2[i][j - 1]
            c3[i][j] += c3[i][j - 1]
    # 3. 各
