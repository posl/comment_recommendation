def check(s1, s2, t):
    if len(s1) + len(s2) + len(t) - 2 < 3 or len(s1) + len(s2) + len(t) - 2 > 16:
        return False
    if t in s1 + s2:
        return False
    return True

if __name__ == '__main__':
    check()