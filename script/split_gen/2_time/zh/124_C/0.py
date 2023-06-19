def minPaints(s):
    #print(s)
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if len(s) > 2:
        if s[0] == s[1]:
            return 1 + minPaints(s[2:])
        else:
            return minPaints(s[1:])
