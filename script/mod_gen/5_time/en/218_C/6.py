def rotate_matrix_90(m):
    return list(zip(*m[::-1]))

if __name__ == '__main__':
    rotate_matrix_90()