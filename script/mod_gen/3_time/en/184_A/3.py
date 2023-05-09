def read_matrix():
    matrix = []
    for i in range(2):
        matrix.append(list(map(int, input().split())))
    return matrix

if __name__ == '__main__':
    read_matrix()