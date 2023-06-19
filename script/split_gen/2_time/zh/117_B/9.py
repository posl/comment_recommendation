def is_polygon(n, l):
    if max(l) < sum(l) - max(l):
        return True
    else:
        return False
