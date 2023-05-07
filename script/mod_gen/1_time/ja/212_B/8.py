def is_weak(x):
    if x[0] == x[1] == x[2] == x[3]:
        return True
    if int(x[0]) == int(x[1]) + 1 and int(x[1]) == int(x[2]) + 1 and int(x[2]) == int(x[3]) + 1:
        return True
    if int(x[0]) == 0 and int(x[1]) == 9 and int(x[2]) == 8 and int(x[3]) == 9:
        return True
    return False

if __name__ == '__main__':
    is_weak()