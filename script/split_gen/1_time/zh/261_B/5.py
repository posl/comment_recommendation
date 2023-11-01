def check(table, N):
    for i in range(N):
        for j in range(N):
            if table[i][j] == 'W':
                if table[j][i] != 'L':
                    return False
            elif table[i][j] == 'L':
                if table[j][i] != '
