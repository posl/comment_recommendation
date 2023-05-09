def rotate(s):
    s = [list(i) for i in s]
    s = list(zip(*s))
    s = [''.join(i) for i in s]
    return s
