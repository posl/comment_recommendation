def check(i,j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return False
    if C[i][j] == '#':
        return False
    return True
