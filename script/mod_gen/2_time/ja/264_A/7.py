def main():
    # 文字列を取得
    atcoder = input()
    # L,Rを取得
    L, R = map(int, input().split())
    # 文字列のL文字目からR文字目までを出力
    print(atcoder[L-1:R])

if __name__ == '__main__':
    main()