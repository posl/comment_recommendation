def rotate_90(l):
    return list(map(list, zip(*l[::-1])))
