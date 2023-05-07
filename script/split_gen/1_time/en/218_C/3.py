def check(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                return False
    return True
