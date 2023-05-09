def is_wonderful_string(s):
    return True if len(s) > 1 and s.islower() and s.isupper() and len(set(s)) == len(s) else False

if __name__ == '__main__':
    is_wonderful_string()