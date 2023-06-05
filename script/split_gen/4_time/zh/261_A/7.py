def get_length(l1, r1, l2, r2):
    if l2 < l1 and r1 < r2:
        return r1 - l1
    elif l1 < l2 and r2 < r1:
        return r2 - l2
    elif l1 < l2 and l2 < r1 and r1 < r2:
        return r1 - l2
    elif l2 < l1 and l1 < r2 and r2 < r1:
        return r2 - l1
    else:
        return 0
