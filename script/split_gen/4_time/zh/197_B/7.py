def check(x, y):
    if (x < 0 or x >= H):
        return False
    if (y < 0 or y >= W):
        return False
    if (S[x][y] == '#'):
        return False
    return True
