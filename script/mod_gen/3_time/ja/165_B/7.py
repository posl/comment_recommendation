def main():
    #入力
    X = int(input())
    #変数
    year = 0
    #処理
    while X > 100:
        X = int(X * 1.01)
        year += 1
    #出力
    print(year)

if __name__ == '__main__':
    main()