def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if len(s) > 100:
        return False
    if not s.isalpha():
        return False
    if not any(c.isupper() for c in s):
        return False
    if not any(c.islower() for c in s):
        return False
    if len(set(s)) != len(s):
        return False
    return True
