def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        if s == t:
            return True
    return False
s = input()
t = input()
