def check(s):
    if s[0::2].islower() and s[1::2].isupper():
        return True
    else:
        return False

if __name__ == '__main__':
    check()