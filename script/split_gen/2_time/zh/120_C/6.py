def max_remove(n, s):
    if n == 1:
        return 0
    if n == 2:
        return 1 if s[0] != s[1] else 0
    if n == 3:
        return 2 if s[0] != s[1] and s[1] != s[2] and s[0] != s[2] else 0
    if n == 4:
        return 3 if (s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[0] != s[2] and s[1] != s[3] and s[0] != s[3]) else 2 if (s[0] != s[1] and s[1] != s[2] and s[0] != s[2]) or (s[0] != s[1] and s[1] != s[3] and s[0] != s[3]) or (s[0] != s[2] and s[2] != s[3] and s[0] != s[3]) or (s[1] != s[2] and s[2] != s[3] and s[1] != s[3]) else 1 if s[0] != s[1] or s[1] != s[2] or s[2] != s[3] else 0
    if n == 5:
        return 4 if (s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4] and s[0] != s[2] and s[1] != s[3] and s[2] != s[4] and s[0] != s[3] and s[1] != s[4] and s[0] != s[4]) else 3 if (s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[0] != s[2] and s[1] != s[3]) or (s[0] != s[1
