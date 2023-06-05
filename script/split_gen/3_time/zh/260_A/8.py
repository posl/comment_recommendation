def solve(s):
    if s[0] == s[1]:
        return s[2]
    elif s[0] == s[2]:
        return s[1]
    elif s[1] == s[2]:
        return s[0]
    else:
        return -1
