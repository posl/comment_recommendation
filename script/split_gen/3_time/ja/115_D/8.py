def main():
    N, X = map(int, input().split())
    # 各レベルの層数を求める
    layer = [1]
    for i in range(N):
        layer.append(2 * layer[-1] + 3)
    # バーガーの下から X 層目のパティの数を求める
    def get_paties(N, X):
        # レベル 0 バーガーの場合
        if N == 0:
            return 0 if X <= 0 else 1
        # レベル N バーガーの下から X 層目
        elif X == 1:
            return 0
        elif X <= 1 + layer[N - 1]:
            return get_paties(N - 1, X - 1)
        elif X == 2 + layer[N - 1]:
            return layer[N - 1] + 1
        elif X <= 2 + 2 * layer[N - 1]:
            return layer[N - 1] + 1 + get_paties(N - 1, X - 2 - layer[N - 1])
        else:
            return 2 * layer[N - 1] + 1
    print(get_paties(N, X))
