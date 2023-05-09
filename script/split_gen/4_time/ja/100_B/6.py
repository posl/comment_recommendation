def main():
    # データ入力
    d, n = map(int, input().split())
    # 処理
    if d == 0:
        if n == 100:
            n = 101
        print(n)
    elif d == 1:
        if n == 100:
            n = 101
        print(n * 100)
    elif d == 2:
        if n == 100:
            n = 101
        print(n * 10000)
