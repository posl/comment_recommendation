def rotate_left(s):
    l = list(s)
    first = l.pop(0)
    l.append(first)
    return ''.join(l)

if __name__ == '__main__':
    rotate_left()