def is_hard_to_read(s):
    if s[0::2].isupper() and s[1::2].islower():
        return True
    else:
        return False
