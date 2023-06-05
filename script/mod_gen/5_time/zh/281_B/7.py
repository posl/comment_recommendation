def check(s):
    if len(s) != 8:
        return False
    if not s[0].isupper() or not s[-1].isupper():
        return False
    if not s[1:-1].isdigit():
        return False
    if int(s[1:-1]) < 100000 or int(s[1:-1]) > 999999:
        return False
    return True

if __name__ == '__main__':
    check()