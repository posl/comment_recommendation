def isLunlun(n):
    s = str(n)
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) > 1:
            return False
    return True
