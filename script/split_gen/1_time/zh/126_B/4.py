def check(s):
    if int(s[0:2]) > 12 or int(s[0:2]) == 0:
        return False
    if int(s[2:]) > 12 or int(s[2:]) == 0:
        return False
    return True
s = input()
