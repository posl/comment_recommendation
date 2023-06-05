def check(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return False
    if s[0] == t[0]:
        return False
    return True

if __name__ == '__main__':
    check()