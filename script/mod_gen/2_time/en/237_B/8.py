def transpose_matrix(matrix):
    #transpose matrix
    return list(map(list, zip(*matrix)))

if __name__ == '__main__':
    transpose_matrix()