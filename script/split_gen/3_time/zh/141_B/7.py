def check(s):
    if len(s) == 1:
        if s[0] == 'L' or s[0] == 'U' or s[0] == 'D':
            return True
        else:
            return False
    else:
        if s[0] == 'R' or s[0] == 'U' or s[0] == 'D':
            return check(s[1:])
        else:
            return False
s = input()
