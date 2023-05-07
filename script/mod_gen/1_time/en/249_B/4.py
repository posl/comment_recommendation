def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if s.islower() or s.isupper():
        return False
    if len(s) != len(set(s)):
        return False
    return True

if __name__ == '__main__':
    is_wonderful_string()