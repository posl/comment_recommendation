def main():
    # 入力受け取り
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 逆順にしておく
    a.reverse()
    c.reverse()
    # 多項式の係数の積を計算
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i] // a[0]
        for j in range(n + 1):
            c[i + j] -= b[i] * a[j]
    # 逆順に戻す
    b.reverse()
    # 結果出力
    print(' '.join(map(str, b)))
