def base26(s):
    res = 0
    for i in s:
        res = res * 26 + (ord(i) - ord('A') + 1)
    return res
