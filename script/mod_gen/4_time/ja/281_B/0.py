def check(s):
    if s[0].isupper() and s[-1].isupper():
        if len(s) == 6:
            if s[1:6].isdecimal():
                return True
    return False
s = input()

if __name__ == '__main__':
    check()