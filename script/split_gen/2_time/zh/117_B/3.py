def check_polygon(n, l):
    l.sort(reverse = True)
    if l[0] < sum(l[1:]):
        return True
    else:
        return False
