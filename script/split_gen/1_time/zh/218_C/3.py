def rotate(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]
