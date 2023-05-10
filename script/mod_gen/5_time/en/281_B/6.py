def check(s):
    if len(s) != 8:
        return False
    if not s[0].isupper():
        return False
    if not s[7].isupper():
        return False
    if not s[1:7].isdigit():
        return False
    if not 100000 <= int(s[1:7]) <= 999999:
        return False
    return True
print('Yes' if check(input()) else 'No')

if __name__ == '__main__':
    check()