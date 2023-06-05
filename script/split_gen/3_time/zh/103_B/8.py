def rotateString(s, t):
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                return True
        return False
s = input()
t = input()
