def isDifficult(s):
    if len(s) < 2:
        return False
    for i in range(0, len(s), 2):
        if s[i].islower():
            return False
    for i in range(1, len(s), 2):
        if s[i].isupper():
            return False
    return True
s = input()

if __name__ == '__main__':
    isDifficult()