def is_black(i,j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if S[i][j] == '#':
        return True
    else:
        return False
