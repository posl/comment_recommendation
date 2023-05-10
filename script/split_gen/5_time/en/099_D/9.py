def get_min_wrongness(c, d, n):
    wrongness = 0
    for i in range(n):
        for j in range(n):
            if (i+j) % 3 == 0:
                wrongness += d[c[i][j]-1][0]
            elif (i+j) % 3 == 1:
                wrongness += d[c[i][j]-1][1]
            elif (i+j) % 3 == 2:
                wrongness += d[c[i][j]-1][2]
    return wrongness
