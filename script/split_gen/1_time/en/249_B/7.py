def is_wonderful_string(s):
    if len(set(s)) != len(s):
        return False
    if s.islower() or s.isupper():
        return False
    return True
