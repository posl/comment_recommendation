def g1(x):
    l = []
    for i in range(len(str(x))):
        l.append(int(str(x)[i]))
    l.sort(reverse=True)
    ret = 0
    for i in range(len(l)):
        ret += l[i] * (10 ** (len(l)-i-1))
    return ret
