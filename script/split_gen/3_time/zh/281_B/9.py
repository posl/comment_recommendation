def check(s):
    if s[0].isupper() and s[-1].isupper() and len(s) == 8:
        try:
            int(s[1:-1])
            return True
        except ValueError:
            return False
    else:
        return False
s = input()
