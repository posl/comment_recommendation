def main():
    # 標準入力から値を取得する
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    # 条件を満たす書き込み方のパターン数を出力する
    print(h1*h2*h3*w1*w2*w3)
