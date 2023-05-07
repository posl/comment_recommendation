def is_wonderful_string(s):
    if s.isupper() or s.islower():
        return False
    for c in s:
        if s.count(c) != 1:
            return False
    return True
s = input()

if __name__ == '__main__':
    is_wonderful_string()