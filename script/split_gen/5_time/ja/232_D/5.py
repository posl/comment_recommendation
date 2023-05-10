def check(x,y):
    if x < 0 or y < 0 or x >= H or y >= W:
        return False
    elif c[x][y] == '#':
        return False
    else:
        return True
