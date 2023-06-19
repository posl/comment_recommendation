def count(s):
    r = 0
    g = 0
    b = 0
    for i in range(len(s)):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    return r, g, b
