def rotate90(matrix):
    return [list(x) for x in zip(*matrix[::-1])]
