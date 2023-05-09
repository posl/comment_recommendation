def main():
    # 標準入力から A, B を取得する
    A, B = map(int, input().split())
    # A + B, A - B, A * B の最大値を求める
    max = A + B
    if max < A - B:
        max = A - B
    if max < A * B:
        max = A * B
    # 最大値を出力する
    print(max)
