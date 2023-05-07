def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if not any(c.isupper() for c in s):
        return False
    if not any(c.islower() for c in s):
        return False
    if len(s) != len(set(s)):
        return False
    return True
s = input()
