def isDifficult(s):
    for i in range(0,len(s)):
        if i%2 == 0 and s[i].isupper():
            return False
        elif i%2 != 0 and s[i].islower():
            return False
    return True
