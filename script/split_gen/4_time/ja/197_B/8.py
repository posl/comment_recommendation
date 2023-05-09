def check(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True
