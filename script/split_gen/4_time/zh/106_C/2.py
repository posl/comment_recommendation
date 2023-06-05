def getKth(s, k):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if k == 1:
            return s[0]
        else:
            return s[1]
    if len(s) == 3:
        if k == 1:
            return s[0]
        elif k == 2:
            return s[1]
        else:
            return s[2]
    if len(s) == 4:
        if k == 1:
            return s[0]
        elif k == 2:
            return s[1]
        elif k == 3:
            return s[2]
        else:
            return s[3]
    else:
        if k <= len(s):
            return s[k-1]
        else:
            return getKth(s[0] * len(s), k % len(s))
