def is_wonderful_string(s):
    if len(s) < 2 or len(s) > 100:
        return False
    if s.islower() or s.isupper():
        return False
    if s.isalnum():
        return False
    if s.isalpha():
        return True
    return False
