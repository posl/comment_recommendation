def rotate90(array):
    return [list(reversed(x)) for x in zip(*array)]
