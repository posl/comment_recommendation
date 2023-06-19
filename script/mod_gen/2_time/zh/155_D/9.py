def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 二分探索
    a.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        x = (l + r) // 2
        # x未満の個数を数える
        num = 0
        for i in range(n):
            if a[i] < 0:
                # 負の数の場合
                l2 = -1
                r2 = n
                while l2 + 1 < r2:
                    c = (l2 + r2) // 2
                    if a[c] * a[i] < x:
                        r2 = c
                    else:
                        l2 = c
                num += n - r2
            else:
                # 0または正の数の場合
                l2 = -1
                r2 = n
                while l2 + 1 < r2:
                    c = (l2 + r2) // 2
                    if a[c] * a[i] < x:
                        l2 = c
                    else:
                        r2 = c
                num += r2
            # 自身の数を引く
            if a[i] * a[i] < x:
                num -= 1
        num //= 2
        if num < k:
            l = x
        else:
            r = x
    print(l)
main()
