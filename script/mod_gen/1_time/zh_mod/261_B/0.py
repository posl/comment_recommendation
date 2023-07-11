def check(x, y):
    if a[x][y] == "D":
        return True
    elif a[x][y] == "W":
        return not check(y, x)
    elif a[x][y] == "L":
        return check(y, x)
    else:
        return False

if __name__ == '__main__':
    check()