def main():
    # 入力値取得
    a, b, c, x = map(int, input().split())
    # 出力
    if x <= a:
        print(1)
    elif a < x <= b:
        print(c / (b - a))
    else:
        print(0)
