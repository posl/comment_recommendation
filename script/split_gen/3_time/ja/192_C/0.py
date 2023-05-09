def g_1(x):
    # x を十進法で表したときの各桁の数字を大きい順に並び替えてできる整数
    return int(''.join(sorted(str(x), reverse=True)))
