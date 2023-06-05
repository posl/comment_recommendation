def check(s, i, j):
    if i + 5 >= len(s) or j + 5 >= len(s[0]):
        return False
    for i2 in range(i, i + 6):
        for j2 in range(j, j + 6):
            if s[i2][j2] == '.':
                return False
    return True

if __name__ == '__main__':
    check()