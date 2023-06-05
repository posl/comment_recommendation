def findSlimeCount(s):
    if len(s) == 0:
        return 0
    res = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += 1
    return res
