def is_wonderful_string(s):
    return s.islower() or s.isupper() or len(s) != len(set(s))

if __name__ == '__main__':
    is_wonderful_string()