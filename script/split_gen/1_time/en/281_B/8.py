def check(s):
    if s[0].isupper() and s[7].isupper() and len(s) == 8:
        if s[1:7].isnumeric() and 100000 <= int(s[1:7]) <= 999999:
            return True
    return False
s = input()
