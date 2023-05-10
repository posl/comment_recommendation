def rotate(l):
    return list(zip(*l[::-1]))

if __name__ == '__main__':
    rotate()