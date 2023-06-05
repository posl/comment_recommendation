def median(l):
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return l[n / 2]
    else:
        return l[n / 2 - 1]
