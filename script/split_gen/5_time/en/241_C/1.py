def solve(n, s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '.':
                s[i][j] = '#'
                if check(n, s):
                    return 'Yes'
                s[i][j] = '.'
    return 'No'
