def isDifficult(s):
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i].islower():
            return False
        if i % 2 == 1 and s[i].isupper():
            return False
    return True
s = input()
print("Yes" if isDifficult(s) else "No")
