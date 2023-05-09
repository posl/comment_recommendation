def rotate(l):
    return [list(x) for x in zip(*l[::-1])]

if __name__ == '__main__':
    rotate()