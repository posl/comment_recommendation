def check(s):
    if s[0] == '0' and s[1] == '0':
        return False
    elif s[2] == '0' and s[3] == '0':
        return False
    else:
        return True

if __name__ == '__main__':
    check()