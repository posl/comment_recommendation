def lunlun(n):
    if n < 10:
        return n
    else:
        # 1桁目の取り出し
        a = n % 10
        # 1桁目以外の取り出し
        b = n // 10
        # 1桁目以外の最大値を取得
        c = max([int(i) for i in str(b)])
        # 1桁目以外の最小値を取得
        d = min([int(i) for i in str(b)])
        # 1桁目の値が最大値の場合
        if a == c:
            return 10 * lunlun(b) + a - 1
        # 1桁目の値が最小値の場合
        elif a == d:
            return 10 * lunlun(b) + a + 1
        # 1桁目の値が最大値と最小値の中間の場合
        else:
            return 10 * lunlun(b) + a
k = int(input())
n = 1
for i in range(k):
    n = lunlun(n)
print(n)
