def median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) // 2
