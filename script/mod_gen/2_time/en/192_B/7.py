def is_hard_to_read(s):
    if len(s) == 1:
        return True
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower():
                return False
        else:
            if s[i].isupper():
                return False
    return True
s = input()

if __name__ == '__main__':
    is_hard_to_read()