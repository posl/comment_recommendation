def solve(s):
    s = list(s)
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            return 2
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            return 1
        else:
            return 0
    res = 0
    for i in range(1, len(s)-1):
        if s[i] == s[i-1] and s[i] == s[i+1]:
            res += 1
            s[i] = str(1 - int(s[i]))
    if s[0] == s[1]:
        res += 1
        s[0] = str(1 - int(s[0]))
    if s[-1] == s[-2]:
        res += 1
        s[-1] = str(1 - int(s[-1]))
    return res
