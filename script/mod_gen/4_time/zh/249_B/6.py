def check(s):
    if s.islower():
        return False
    elif s.isupper():
        return False
    elif len(s) % 2 != 0:
        return False
    else:
        for i in range(0, len(s), 2):
            if s[i].islower() or s[i+1].isupper():
                return False
        return True

if __name__ == '__main__':
    check()