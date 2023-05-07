def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    # 1. Aの中の最小値を求める
    # 2. 最小値を引く
    # 3. Aの中の最小値を求める
    # 4. 2.と3.を繰り返す
    # 5. 繰り返しの回数を出力する
    # 1. Aの中の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])
    # 2. 最小値を引く
    for i in range(H):
        for j in range(W):
            A[i][j] -= min_A
    # 3. Aの中の最小値を求める
    min_A = min([min(A[i]) for i in range(H)])
    # 4. 2.と3.を繰り返す
    while min_A != 0:
        # 2. 最小値を引く
        for i in range(H):
            for j in range(W):
                A[i][j] -= min_A
        # 3. Aの中の最小値を求める
        min_A = min([min(A[i]) for i in range(H)])
    # 5. 繰り返しの回数を出力する
    print(min_A)
