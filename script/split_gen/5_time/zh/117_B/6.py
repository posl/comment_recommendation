def is_polygon(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return True
    else:
