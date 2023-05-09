def main():
    # Nを取得する
    N = int(input())
    # aを取得する
    a = list(map(int, input().split()))
    # print(N)
    # print(a)
    # 操作回数をカウントする変数を定義する
    count = 0
    # aの要素を順番に操作する
    for i in range(N):
        # aの要素が奇数の場合は終了する
        if a[i] % 2 != 0:
            continue
        # aの要素が偶数の場合は操作する
        else:
            # 操作回数をカウントする
            count += 1
            # aの要素を2で割る
            a[i] = a[i] / 2
            # aの要素が偶数になるまで操作する
            while a[i] % 2 == 0:
                # 操作回数をカウントする
                count += 1
                # aの要素を2で割る
                a[i] = a[i] / 2
    # 結果を出力する
    print(count)
