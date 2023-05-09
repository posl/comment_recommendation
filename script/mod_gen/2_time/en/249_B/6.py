def is_wonderful_string(s):
    if not s:
        return False
    if len(s) < 2:
        return False
    if len(s) > 100:
        return False
    if not s.isalpha():
        return False
    if not s.islower() and not s.isupper():
        return False
    if len(set(s)) != len(s):
        return False
    return True

if __name__ == '__main__':
    is_wonderful_string()