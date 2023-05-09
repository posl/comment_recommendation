def rotate(s):
    return list(map(list, zip(*s[::-1])))
