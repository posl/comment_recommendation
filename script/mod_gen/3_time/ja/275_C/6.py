def check(p, x, y):
    if x < 0 or x >= 9 or y < 0 or y >= 9:
        return False
    if p[x][y] == '#':
        return True
    return False

if __name__ == '__main__':
    check()