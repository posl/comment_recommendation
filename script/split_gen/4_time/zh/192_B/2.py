def is_hard_to_read(s):
    if len(s) == 0:
        return True
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].islower():
                return False
        else:
            if s[i].isupper():
                return False
    return True
