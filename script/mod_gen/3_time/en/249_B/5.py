def is_wonderful(s):
    s = s.lower()
    if len(s) < 2:
        return False
    if s.islower():
        return False
    if s.isupper():
        return False
    if len(set(s)) != len(s):
        return False
    return True

if __name__ == '__main__':
    is_wonderful()