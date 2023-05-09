def solve():
    # 標準入力から abc を取得する
    abc = input()
    # abc を int 型に変換する
    abc = int(abc)
    # bca を計算する
    bca = abc // 100 + (abc // 10) % 10 * 100 + abc % 10 * 10
    # cab を計算する
    cab = abc % 10 * 100 + abc // 100 + (abc // 10) % 10 * 10
    # abc + bca + cab を計算する
    result = abc + bca + cab
    # 結果を出力する
    print(result)

if __name__ == '__main__':
    solve()