def is_hard_read(s):
    l = len(s)
    for i in range(0, l):
        if i%2 == 0:
            if s[i].islower():
                return False
        else:
            if s[i].isupper():
                return False
    return True
