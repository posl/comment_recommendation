def main():
    # データ入力
    a, b, c, d = map(int, input().split())
    # 判定
    if a < b * c:
        print(-1)
    else:
        # 操作回数の計算
        count = 0
        while a > b * d:
            a += c
            count += 1
        print(count)
