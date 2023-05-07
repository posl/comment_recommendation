def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if s.islower() or s.isupper():
        return False
    if len(s) != len(set(s)):
        return False
    return True
