def main():
    # 入力
    a, b, c, d, e = map(int, input().split())
    # 処理
    set_a = set([a, b, c, d, e])
    # 出力
    print(len(set_a))
