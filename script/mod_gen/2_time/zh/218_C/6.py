def rotate_matrix(m):
    return [list(reversed(i)) for i in zip(*m)]

if __name__ == '__main__':
    rotate_matrix()