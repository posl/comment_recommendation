def is_wonderful_string(s):
    if not s.islower() and not s.isupper():
        return False
    if not s.islower():
        if s[0].isupper():
            return True
        else:
            return False
    if not s.isupper():
        if s[0].islower():
            return True
        else:
            return False
s = input()
