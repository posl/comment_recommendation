def func(s,t):
    if not s or not t or len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if ord(s[i]) > ord(t[i]):
                return False
            else:
                return True
    return False
