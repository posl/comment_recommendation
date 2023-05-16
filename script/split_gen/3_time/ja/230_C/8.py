def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1 つめの操作で塗る黒マスの数を求める
    # 上下左右の端点から塗るマスの数を求める
    # 端点の座標は (A, B) とする
    # 上端点から塗るマスの数を求める
    # max(1-A, 1-B) <= k <= min(N-A, N-B)
    # 上端点から塗るマスの数
    # (N-B) - max(1-A, 1-B) + 1
    # 下端点から塗るマスの数
    # (N-A) - max(1-B, 1-A) + 1
    # 左端点から塗るマスの数
    # (N-A) - max(1-B, 1-A) + 1
    # 右端点から塗るマスの数
    # (N-B) - max(1-A, 1-B) + 1
    # 上端点から塗るマスの数
    tate = min(N-B, N-A) - max(1-A, 1-B) + 1
    # 下端点から塗るマスの数
    yoko = min(N-A, N-B) - max(1-B, 1-A) + 1
    # 1 つめの操作で塗るマスの数
    cnt1 = tate * yoko
    # 2 つめの操作で塗る黒マスの数を求める
    # 上下左右の端点から塗るマスの数を求める
    # 端点の座標は (A, B) とする
    # 上端点から塗るマスの数を求める
    # max(1-A, B-N) <= k <= min(N-A, B-1)
    # 上端点から塗るマ