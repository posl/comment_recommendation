def is_wonderful ( s ):
    if s.islower() or s.isupper():
        return False
    if len (s) != len (set (s)):
        return False
    return True
s = input ()

if __name__ == '__main__':
    is_wonderful()