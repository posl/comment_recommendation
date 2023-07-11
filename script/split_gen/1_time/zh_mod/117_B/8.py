def is_polygon(L):
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        return True
    else:
        return False
