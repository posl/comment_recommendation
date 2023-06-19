def check(s):
    if not s.islower() and not s.isupper():
        return False
    if not s.islower():
        return False
    if not s.isupper():
        return False
    return True
s = input()
print('Yes' if check(s) else 'No')
