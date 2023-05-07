def bingo_check(a):
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2]:
            return True
        elif a[0][i] == a[1][i] == a[2][i]:
            return True
    if a[0][0] == a[1][1] == a[2][2]:
        return True
    elif a[0][2] == a[1][1] == a[2][0]:
        return True
    return False

if __name__ == '__main__':
    bingo_check()