def is_wonderful_string(s):
    return s.islower() or s.isupper() or len(s) != len(set(s))
