def getNumOfX(H, W, C):
    X = []
    for j in range(W):
        numOfX = 0
        for i in range(H):
            if C[i][j] == "#":
                numOfX += 1
        X.append(numOfX)
    return X
