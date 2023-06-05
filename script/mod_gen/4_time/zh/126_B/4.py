def check(s):
    if s[0] == '0' and s[1] == '0':
        return False
    if s[2] == '0' and s[3] == '0':
        return False
    return True

if __name__ == '__main__':
    check()