def check_6x6(m, i, j):
    # check horizontal
    if j <= len(m[i]) - 6:
        for k in range(j, j + 6):
            if m[i][k] != '#':
                break
        else:
            return True
    # check vertical
    if i <= len(m) - 6:
        for k in range(i, i + 6):
            if m[k][j] != '#':
                break
        else:
            return True
    # check diagonal
    if i <= len(m) - 6 and j <= len(m[i]) - 6:
        for k in range(6):
            if m[i + k][j + k] != '#':
                break
        else:
            return True
    if i <= len(m) - 6 and j >= 5:
        for k in range(6):
            if m[i + k][j - k] != '#':
                break
        else:
            return True
    return False
