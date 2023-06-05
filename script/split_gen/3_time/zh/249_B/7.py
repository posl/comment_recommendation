def check(s):
    if len(s) < 2:
        return False
    if s[0].isupper() and s[1].islower():
        return True
    if s[0].islower() and s[1].isupper():
        return True
    return False
s = input()
