def rotate(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

if __name__ == '__main__':
    rotate()