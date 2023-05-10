def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(N, K, A, XY)
    # 人iの座標を(x_i, y_i)とすると、人iが明かりR_iを持つとき、
    # 人iが照らされる領域は、(x_i - R_i, x_i + R_i) x (y_i - R_i, y_i + R_i)の長方形の内部全体（境界を含む）となる
    # この長方形の内部全体が、他の人の長方形の内部全体と重ならないように、R_iを決める必要がある
    # このR_iの最小値を求める
    # 人iの座標を(x_i, y_i)とすると、人iが明かりR_iを持つとき、
    # 人iが照らされる領域は、(x_i - R_i, x_i + R_i) x (y_i - R_i, y_i + R_i)の長方形の内部全体（境界を含む）となる
    # この長方形の内部全体が、他の人の長方形の内部全体と重ならないように、R_iを決める必要がある
    # このR_iの最小値を求める
    # 人iの座標を(x_i, y_i)とするとき、人iが明かりR_iを持つとき、
    # 人iが照らされる領域は、(x_i - R_i, x_i + R_i) x (y_i - R_i, y_i + R_i)の長方形の内部全体（境界を含む）となる
