def main():
    # 文字列の定義
    atcoder = "atcoder"
    # 入力
    L, R = map(int, input().split())
    # 出力
    print(atcoder[L-1:R])

if __name__ == '__main__':
    main()