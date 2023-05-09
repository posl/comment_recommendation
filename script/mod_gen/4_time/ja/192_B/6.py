def check(s):
    if len(s) == 1:
        return True
    for i in range(1, len(s), 2):
        if not s[i].islower():
            return False
    for i in range(0, len(s), 2):
        if not s[i].isupper():
            return False
    return True
s = input()

if __name__ == '__main__':
    check()