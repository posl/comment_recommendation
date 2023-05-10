def check(s):
    if not s[0].isupper():
        return False
    if not s[-1].isupper():
        return False
    if not 100000 <= int(s[1:-1]) <= 999999:
        return False
    return True
s = input()
print('Yes' if check(s) else 'No')

if __name__ == '__main__':
    check()