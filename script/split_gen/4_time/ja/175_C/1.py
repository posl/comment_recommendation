def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    #a = int(input())
    # スペース区切りの整数の入力
    #b, c = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= d * k:
        print(x - d * k)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)
    return 0
