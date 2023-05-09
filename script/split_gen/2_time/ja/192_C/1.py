def g1(x):
    s = list(str(x))
    s.sort(reverse=True)
    return int("".join(s))
