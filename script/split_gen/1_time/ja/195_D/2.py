def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        # ボールを箱に入れる
        # 重さの重複を許す
        # 価値の合計を最大化
        # 価値の合計が最大になるような箱の選び方を
