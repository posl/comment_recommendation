def isMatch(s, t):
    if len(s) > len(t):
        return False
    if s == t:
        return True
    if len(s) == 1:
        return False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s1 = s[0:i+1] + s[i+1:]
            if isMatch(s1, t):
                return True
    return False
s = input()
t = input()
