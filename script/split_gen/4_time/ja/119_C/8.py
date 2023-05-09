def concat(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1[-1] > l2[-1]:
        return concat(l2, l1)
    else:
        return concat(l1[:-1], l2) + [l1[-1]]
