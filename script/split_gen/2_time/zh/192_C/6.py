def check(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower():
                continue
            else:
                return False
        else:
            if s[i].isupper():
                continue
            else:
                return False
    return True
