def check(s, a):
    if len(s) == 0:
        return True
    if len(s) == 1 and s[0] == a:
        return False
    for i in range(1, len(s)):
        if s[i] == a:
            return False
    return True

if __name__ == '__main__':
    check()