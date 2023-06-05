def get_matrix():
    H, W = map(int, input().split())
    matrix = []
    for i in range(H):
        row = input()
        matrix.append(row)
    return matrix
