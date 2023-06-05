def checkDifficult(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i].islower():
            continue
        elif i % 2 == 1 and s[i].isupper():
            continue
        else:
            return False
    return True
