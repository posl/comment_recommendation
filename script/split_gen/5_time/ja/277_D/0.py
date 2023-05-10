def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if n == 1:
        if a[0] == 0:
            print(0)
        else:
            print((m-1) - a[0])
        return
    # 0の個数
    zero = 0
    for i in range(n):
        if a[i] == 0:
            zero += 1
        else:
            break
    # 0がある場合は、0の個数分のカードが必要
    if zero > 0:
        n -= zero
        if n == 0:
            print(0)
            return
    # 0がない場合は、1枚は必要
    else:
        n -= 1
    # 0がない場合は、1枚は必要
    # 0がある場合は、0の個数分のカードが必要
    # それ以外は、0の個数を1枚として、残りのカード枚数として、最大値を計算する
    # その最大値が、m-1になる
    # そのm-1から、0の個数分のカードの値を引く
    # それが答え
    print((m-1) - a[n-1])
