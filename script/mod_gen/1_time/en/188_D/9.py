def main():
    #入力
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for i in range(N)]
    #日付と利用料金のリストを作成
    date_price = list()
    for i in range(N):
        date_price.append([abc[i][0], abc[i][2]])
        date_price.append([abc[i][1]+1, -abc[i][2]])
    #日付と利用料金のリストを日付でソート
    date_price.sort()
    #日付と利用料金のリストを使って計算
    date = date_price[0][0]
    price = date_price[0][1]
    total_price = date_price[0][1]
    for i in range(1, 2*N):
        if date_price[i][0] == date:
            price += date_price[i][1]
            total_price += date_price[i][1]
        else:
            date = date_price[i][0]
            price += date_price[i][1]
            if price < C:
                total_price += price
            else:
                total_price += C
    #出力
    print(total_price)

if __name__ == '__main__':
    main()