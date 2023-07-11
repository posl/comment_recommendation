def check_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if i != j:
                if table[i][j] == 'W' and table[j][i] != 'L':
                    return False
                elif table[i][j] == 'L' and table[j][i] != 'W':
                    return False
                elif table[i][j] == 'D' and table[j][i] != 'D':
