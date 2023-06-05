def rotate_left(s):
    l = list(s)
    first = l.pop(0)
    l.append(first)
    return ''.join(l)
