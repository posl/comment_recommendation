def rotate(s):
    n = len(s)
    t = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][n-i-1] = s[i][j]
    return t
