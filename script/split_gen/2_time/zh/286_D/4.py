def getMinCost(s, a, b):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return a
    if len(s) == 2:
        if s[0] == s[1]:
            return 0
        else:
            return min(a, b)
    if s[0] == s[-1]:
        return getMinCost(s[1:-1], a, b)
    else:
        return min(getMinCost(s[1:], a, b) + a, getMinCost(s[:-1], a, b) + a, getMinCost(s[1:-1], a, b) + b)
