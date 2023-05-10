def rotate_clockwise(matrix):
    """Rotates a matrix clockwise"""
    return [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]

if __name__ == '__main__':
    rotate_clockwise()