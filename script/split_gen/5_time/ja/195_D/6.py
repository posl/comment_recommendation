def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X.sort(reverse=True)
    for L, R in Query:
        # L-1までの箱の中で価値が最大の荷物を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物