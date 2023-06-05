def isDifficult(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i].islower():
            return False
        if i % 2 == 1 and s[i].isupper():
            return False
    return True

if __name__ == '__main__':
    isDifficult()