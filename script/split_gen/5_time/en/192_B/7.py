def is_hard_to_read(s):
    if len(s) == 1:
        return s.islower()
    else:
        return s[::2].islower() and s[1::2].isupper()
