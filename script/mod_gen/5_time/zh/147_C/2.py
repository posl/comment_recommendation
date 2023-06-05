def check(a, x, y, honest):
    for i in range(a):
        if (x[i] in honest) and (y[i] == 1):
            continue
        elif (x[i] in honest) and (y[i] == 0):
            return False
        elif (x[i] not in honest) and (y[i] == 1):
            return False
        elif (x[i] not in honest) and (y[i] == 0):
            continue
    return True

if __name__ == '__main__':
    check()