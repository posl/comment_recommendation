def rotate(matrix):
    return list(zip(*matrix[::-1]))

if __name__ == '__main__':
    rotate()