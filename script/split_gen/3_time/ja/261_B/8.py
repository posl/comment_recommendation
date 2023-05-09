def check(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == 'W':
                if input[j][i] != 'L':
                    return False
            elif input[i][j] == 'L':
                if input[j][i] != 'W':
                    return False
            elif input[i][j] == 'D':
                if input[j][i] != 'D':
                    return False
    return True
