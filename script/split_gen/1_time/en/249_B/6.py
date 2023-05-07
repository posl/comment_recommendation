def is_wonderful(s):
    if len(s) > 100:
        return False
    if not s.isalpha():
        return False
    if not s.islower() and not s.isupper():
        return False
    if len(s) != len(set(s)):
        return False
    return True
