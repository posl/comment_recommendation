def is_wonderful(s):
    s = s.lower()
    if s.islower():
        return False
    elif s.isupper():
        return False
    elif len(s) != len(set(s)):
        return False
    else:
        return True

if __name__ == '__main__':
    is_wonderful()