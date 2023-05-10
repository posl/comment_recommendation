def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    # X座標とY座標のリストを作る
    X = [x for x, y in XY]
    Y = [y for x, y in XY]
    # 左右の向きを判定する
    is_right = [s == 'R' for s in S]
    # X座標とY座標をそれぞれソートする
    X.sort()
    Y.sort()
    # X座標とY座標の差分をとる
    X_diff = [X[i + 1] - X[i] for i in range(N - 1)]
    Y_diff = [Y[i + 1] - Y[i] for i in range(N - 1)]
    # 左右の向きによって、差分の正負を変える
    for i in range(N - 1):
        if not is_right[i]:
            X_diff[i] *= -1
        if not is_right[i + 1]:
            Y_diff[i] *= -1
    # 差分が正負が逆になっている場合は衝突する
    if (all([x > 0 for x in X_diff]) and all([y < 0 for y in Y_diff])) or (all([x < 0 for x in X_diff]) and all([y > 0 for y in Y_diff])):
        print('Yes')
    else:
        print('No')
