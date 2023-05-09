def is_hard_to_read(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            return False
        if i % 2 == 1 and s[i].islower():
            return False
    return True

if __name__ == '__main__':
    is_hard_to_read()