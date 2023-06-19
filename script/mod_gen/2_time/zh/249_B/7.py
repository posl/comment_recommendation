def check(s):
    if s.islower() or s.isupper():
        return False
    if s.isalpha():
        if s[0].isupper() and s[-1].islower():
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    check()