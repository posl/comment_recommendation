def check(s):
    if not s.islower():
        return False
    if not s.isupper():
        return False
    if len(s) != len(set(s)):
        return False
    return True
s = input()
