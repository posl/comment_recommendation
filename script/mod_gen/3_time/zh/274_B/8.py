def get_X(W,H,C):
    X = []
    for j in range(W):
        count = 0
        for i in range(H):
            if C[i][j] == "#":
                count += 1
        X.append(count)
    return X

if __name__ == '__main__':
    get_X()