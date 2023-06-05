def check(s, t):
    if len(t) != len(s) + 1:
        return False
    if s == t[:-1]:
        return True
    return False

if __name__ == '__main__':
    check()