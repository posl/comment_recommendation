def check(n, m, s, t):
    for i in range(n):
        if len(s[i]) == 0:
            return False
    for i in range(m):
        if len(t[i]) == 0:
            return False
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                return False
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if t[i] == t[j]:
                return False
    for i in range(n):
        for j in range(m):
            if t[j] == s[i]:
                return False
    return True

if __name__ == '__main__':
    check()