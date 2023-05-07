def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #辞書型を使って、文字列とその出現回数を管理する
    d = {}
    for s in S:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    #辞書型のvalueを基準に降順ソートしたリストを作成する
    #辞書型のkeyを基準に降順ソートしたリストを作成する
    #辞書型のkeyを基準に昇順ソートしたリストを作成する
    d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
    d_sorted_key = sorted(d.items(), key=lambda x: x[0])
    d_sorted_value = sorted(d.items(), key=lambda x: x[1])
    #出現回数が最大の文字列を出力する
    for i in range(len(d_sorted)):
        if d_sorted[i][1] == d_sorted[0][1]:
            print(d_sorted[i][0])
        else:
            break

if __name__ == '__main__':
    main()