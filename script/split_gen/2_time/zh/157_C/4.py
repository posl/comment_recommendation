def bingo(x):
    for i in range(3):
        if x[i][0] == x[i][1] == x[i][2] == 1:
            return True
    for i in range(3):
        if x[0][i] == x[1][i] == x[2][i] == 1:
            return True
    if x[0][0] == x[1][1] == x[2][2] == 1:
        return True
    if x[0][2] == x[1][1] == x[2][0] == 1:
        return True
    return False
