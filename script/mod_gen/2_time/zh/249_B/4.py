def iswonderful(s):
    if len(s) <= 1:
        return False
    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return True
        else:
            return False
    if len(s) > 2:
        if s.islower():
            return False
        if s.isupper():
            return False
        if s[0].isupper() and s[1].islower():
            return iswonderful(s[2:])
        if s[0].islower() and s[1].isupper():
            return iswonderful(s[1:])
        if s[0].isupper() and s[1].isupper():
            return iswonderful(s[1:])
        if s[0].islower() and s[1].islower():
            return iswonderful(s[1:])

if __name__ == '__main__':
    iswonderful()