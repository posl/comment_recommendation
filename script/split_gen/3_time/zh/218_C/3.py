def rotate90(s):
    return [''.join(x) for x in zip(*s[::-1])]
