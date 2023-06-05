def check(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 'W':
                if table[j][i] != 'L':
                    return False
            elif table[i][j] == 'L':
                if table[j][i] != 'W':
                    return False
            elif table[i][j] == 'D':
                if table[j][i] != 'D':
                    return False
    return True

if __name__ == '__main__':
    check()