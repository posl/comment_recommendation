def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #print(X)
        #print(W)
        #print(V)
        #print()
        # 箱を選ぶ
        box = X[:L - 1] + X[R:]
        #print(box)
        #print()
        # 箱に入れる荷物を選ぶ
        # 箱の大きさでソートする
        box.sort()
        #print(box)
        #print()
        # 荷物を大きさでソートする
        W_V = sorted(zip(W, V), key=lambda x: x[0])
        #print(W_V)
        #print()
        # 荷物を箱に入れる
        value = 0
        for w, v in W_V:
            for i, b in enumerate(box):
                if w <= b:
                    value += v
                    box[i] = 0
                    break
        print(value)
