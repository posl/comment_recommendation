def rotate(s):
    return list(map(list, zip(*s[::-1])))

if __name__ == '__main__':
    rotate()