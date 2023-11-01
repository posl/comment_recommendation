def is_polygon(l):
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        return True
    return False
