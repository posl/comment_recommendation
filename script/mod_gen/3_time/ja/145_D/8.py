def main():
    # 入力
    X, Y = map(int, input().split())
    # 0,0に戻れるか判定
    if (X + Y) % 3 != 0:
        print(0)
        return
    # 0,0に戻れる場合
    # 0,0からの距離を求める
    dist = (X + Y) // 3
    # 0,0からの距離が遠い方の座標を求める
    if X > Y:
        x = dist
        y = dist - X
    else:
        x = dist - Y
        y = dist
    # nCrを求める
    n = x + y
    r = x
    # nCrの計算
    ans = 1
    for i in range(n, n - r, -1):
        ans *= i
    for i in range(1, r + 1):
        ans //= i
    # 余りを求める
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()