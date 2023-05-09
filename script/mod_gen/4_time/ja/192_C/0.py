def g1(x):
    #x を十進法で表したときの各桁の数字を大きい順に並び替えてできる整数
    str_x = str(x)
    list_str_x = sorted(str_x, reverse=True)
    return int("".join(list_str_x))

if __name__ == '__main__':
    g1()