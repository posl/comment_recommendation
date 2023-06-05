def check(s):
    if len(s) != 8:
        return False
    if s[0] < 'A' or s[0] > 'Z':
        return False
    if s[7] < 'A' or s[7] > 'Z':
        return False
    if s[1:7].isdecimal():
        if int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999:
            return True
        else:
            return False
    else:
        return False
s = input()

if __name__ == '__main__':
    check()