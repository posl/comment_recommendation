def check(s):
    if len(s) != 7:
        return False
    if s[0].isupper() and s[6].isupper():
        if s[1:6].isdigit():
            return True
    return False
s = input()
