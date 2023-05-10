def swap(s, t):
    if s == t:
        return True
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            return True
    return False
