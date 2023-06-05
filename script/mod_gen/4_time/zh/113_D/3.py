def get_matrix(H,W):
    matrix = []
    for i in range(H+1):
        matrix.append([])
        for j in range(W):
            matrix[i].append(0)
    return matrix

if __name__ == '__main__':
    get_matrix()