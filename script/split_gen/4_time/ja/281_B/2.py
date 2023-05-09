def check(s):
    if s[0].isupper():
        if s[-1].isupper():
            if len(s) == 6:
                if s[1:5].isdecimal():
                    return True
    return False
s = input()
