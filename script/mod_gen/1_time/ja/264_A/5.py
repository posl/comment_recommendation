def main():
    # 文字列の入力
    atcoder = input()
    # 整数の入力
    L, R = map(int, input().split())
    # 出力
    print(atcoder[L-1:R])

if __name__ == '__main__':
    main()