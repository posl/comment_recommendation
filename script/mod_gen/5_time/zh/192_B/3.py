def is_easy(s):
    if len(s) == 1:
        return True
    for i in range(1, len(s), 2):
        if s[i].islower():
            return False
    for i in range(0, len(s), 2):
        if s[i].isupper():
            return False
    return True

if __name__ == '__main__':
    is_easy()