def check(s):
    if s[0].isupper() and s[-1].isupper():
        if len(s) == 8:
            if s[1:-1].isdigit():
                if int(s[1:-1]) >= 100000 and int(s[1:-1]) <= 999999:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
s = input()
