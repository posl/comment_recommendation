def main():
    #入力
    X = int(input())
    #初期値
    year = 0
    money = 100
    #処理
    while money < X:
        money = int(money * 1.01)
        year += 1
    #出力
    print(year)

if __name__ == '__main__':
    main()