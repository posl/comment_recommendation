def g1(x):
    s = str(x)
    l = list(s)
    l.sort(reverse=True)
    s = "".join(l)
    return int(s)
