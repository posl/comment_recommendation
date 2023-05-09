def main():
    s = input()
    q = int(input())
    # 3回目の置換で元の文字列に戻る
    s = s * 3
    # 置換の回数
    t = 0
    # 置換の回数と文字列の長さのペア
    d = {}
    # 置換の回数と文字列の長さのペアを作成
    for i in range(3):
        t += 1
        d[t] = len(s)
        s = s.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
    # 置換の回数と文字列の長さのペアを作成
    for i in range(q):
        t, k = map(int, input().split())
        # 置換の回数が3回以上の場合は、置換の回数を3で割った余りに置換する
        if t > 3:
            t %= 3
        # 置換の回数が1の場合
        if t == 1:
            print(s[k - 1])
        # 置換の回数が2の場合
        elif t == 2:
            print(s[k + d[1] - 1])
        # 置換の回数が3の場合
        else:
            print(s[k + d[2] - 1])
