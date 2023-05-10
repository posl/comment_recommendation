def wrongness(D, c, N, C):
    w = 0
    for i in range(N):
        for j in range(N):
            if (i+j) % 3 == 0:
                w += D[c[i][j]-1][0]
            elif (i+j) % 3 == 1:
                w += D[c[i][j]-1][1]
            else:
                w += D[c[i][j]-1][2]
    return w

if __name__ == '__main__':
    wrongness()