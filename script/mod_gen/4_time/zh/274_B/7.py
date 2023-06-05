def find_num_of_boxes(H, W, C):
    # print(H, W, C)
    X = [[0 for i in range(W)] for i in range(H)]
    # print(X)
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[i][j] = 1
    # print(X)
    for j in range(W):
        for i in range(1, H):
            if X[i][j] == 1:
                X[0][j] += 1
    # print(X)
    for j in range(W):
        for i in range(1, H):
            if X[H - i - 1][j] == 1:
                X[H - 1][j] += 1
    # print(X)
    for i in range(H):
        for j in range(1, W):
            if X[i][j] == 1:
                X[i][0] += 1
    # print(X)
    for i in range(H):
        for j in range(1, W):
            if X[i][W - j - 1] == 1:
                X[i][W - 1] += 1
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 4:
                X[i][j] = 0
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 1:
                X[i][j] = 0
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 2:
                X[i][j] = 1
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 3:
                X[i][j] = 1
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 0:
                X[i][j] = '.'
    # print(X)
    for i in range(H):
        for j in range(W):
            if X[i][j] == 1:
                X[i][j] =

if __name__ == '__main__':
    find_num_of_boxes()