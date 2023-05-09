def check(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return True
    else:
        return False

if __name__ == '__main__':
    check()