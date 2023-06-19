def check(s):
    if len(s) != 9:
        return False
    if not s[0].isupper():
        return False
    if not s[8].isupper():
        return False
    if not s[1:7].isdigit():
        return False
    if int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        return False
    return True
s = input()
