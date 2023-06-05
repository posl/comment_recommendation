def check(s):
    if int(s[:2]) > 12:
        return False
    if int(s[2:]) > 12:
        return False
    return True

if __name__ == '__main__':
    check()