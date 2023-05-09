def main():
    # 1行目を取得
    a, b = map(int, input().split())
    # 2行目を取得
    c, d = map(int, input().split())
    # x-yの最大値を出力
    print(max(b - c, d - a, b - d, c - a))

if __name__ == '__main__':
    main()