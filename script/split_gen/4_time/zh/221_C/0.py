def div(n):
    if n < 10:
        return 0
    s = str(n)
    l = len(s)
    res = 0
    for i in range(1,l):
        a = int(s[:i])
        b = int(s[i:])
        if a * b > res:
            res = a * b
    return res
