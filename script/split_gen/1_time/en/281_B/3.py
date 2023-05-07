def check(s):
    if s[0].isupper() and s[-1].isupper():
        if s[1:-1].isdigit():
            if 100000 <= int(s[1:-1]) <= 999999:
                return True
    return False
s = input()
