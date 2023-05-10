def is_hard_to_read(s):
    if len(s) == 1:
        return s.islower()
    else:
        for i in range(0, len(s), 2):
            if not s[i].isupper():
                return False
        for i in range(1, len(s), 2):
            if not s[i].islower():
                return False
        return True

if __name__ == '__main__':
    is_hard_to_read()