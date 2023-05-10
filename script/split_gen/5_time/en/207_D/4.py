def check(s, t):
    for i in range(len(s)):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            return False
    return True
