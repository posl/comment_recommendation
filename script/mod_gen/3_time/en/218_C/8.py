def rotate90(array):
    return [list(reversed(x)) for x in zip(*array)]

if __name__ == '__main__':
    rotate90()