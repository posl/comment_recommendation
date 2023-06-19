def get_nickname(s, t):
    for i in range(len(s)):
        if s[i] == t[i]:
            return s[i]
    return ""
