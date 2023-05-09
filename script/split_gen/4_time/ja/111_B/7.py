def main():
    # 標準入力受け取り
    n = int(input())
    # 初期化
    x = 0
    # ループ
    while x < 1000:
        if x >= n:
            print(x)
            break
        else:
            x += 111
