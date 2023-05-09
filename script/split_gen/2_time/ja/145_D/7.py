def main():
    # 入力
    X, Y = map(int, input().split())
    # 処理
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    # 二項係数の計算
    # 組み合わせの数を求める
    # 10^9+7 で割った余りを求める
    def comb(n, r):
        x = 1
        y = 1
        for i in range(n, n - r, -1):
            x *= i
            x %= 1000000007
        for i in range(1, r + 1):
            y *= i
            y %= 1000000007
        return (x * pow(y, 1000000005, 1000000007)) % 1000000007
    print(comb(N, X))
