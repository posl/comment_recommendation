def find_unique_char(s):
    if s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
        return s[0]
    elif s[0] == s[1] and s[1] != s[2]:
        return s[2]
    elif s[0] != s[1] and s[1] == s[2]:
        return s[0]
    elif s[0] == s[1] and s[1] == s[2]:
        return -1
