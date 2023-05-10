def is_hard_to_read(s):
    return s[::2].islower() and s[1::2].isupper()

if __name__ == '__main__':
    is_hard_to_read()