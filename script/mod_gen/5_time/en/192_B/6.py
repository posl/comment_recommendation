def check_string(s):
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i].islower():
                continue
            else:
                return False
        else:
            if s[i].isupper():
                continue
            else:
                return False
    return True

if __name__ == '__main__':
    check_string()