def check(s,t):
    n = len(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                return False
    return True
