def check_hard_read(s):
    if len(s) < 1 or len(s) > 1000:
        return False
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i].isupper():
            continue
        elif i % 2 == 1 and s[i].islower():
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    check_hard_read()