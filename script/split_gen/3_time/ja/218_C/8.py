def rotate(l):
    return [list(x) for x in zip(*l[::-1])]
