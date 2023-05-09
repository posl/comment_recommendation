def search(s, t, n, m):
    for i in range(0, m):
        if t[i] == s:
            return False
    return True
