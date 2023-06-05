def check(n, s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                if i + 5 < n and s[i + 1][j] == '#' and s[i + 2][j] == '#' and s[i + 3][j] == '#' and s[i + 4][j] == '#' and s[i + 5][j] == '#':
                    return True
                if j + 5 < n and s[i][j + 1] == '#' and s[i][j + 2] == '#' and s[i][j + 3] == '#' and s[i][j + 4] == '#' and s[i][j + 5] == '#':
                    return True
                if i + 5 < n and j + 5 < n and s[i + 1][j + 1] == '#' and s[i + 2][j + 2] == '#' and s[i + 3][j + 3] == '#' and s[i + 4][j + 4] == '#' and s[i + 5][j + 5] == '#':
                    return True
                if i + 5 < n and j - 5 >= 0 and s[i + 1][j - 1] == '#' and s[i + 2][j - 2] == '#' and s[i + 3][j - 3] == '#' and s[i + 4][j - 4] == '#' and s[i + 5][j - 5] == '#':
                    return True
    return False
