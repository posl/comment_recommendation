def check(s):
    if s[0] == '0':
        if s[1] in ['0','1','2','3','4','5','6','7','8','9']:
            return True
        else:
            return False
    elif s[0] == '1':
        if s[1] in ['0','1','2']:
            return True
        else:
            return False
    else:
        return False
s = input()
