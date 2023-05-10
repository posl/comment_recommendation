def replace(s, t):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in s[i+1:]:
                s[i+1+s[i+1:].index(s[i])] = t[i]
            else:
                return False
    return True
s = input()
t = input()
