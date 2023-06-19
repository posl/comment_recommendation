def check(x):
    s = str(x)
    if len(s) % 2 == 1:
        return False
    else:
        return s[:len(s)//2] == s[len(s)//2:]
