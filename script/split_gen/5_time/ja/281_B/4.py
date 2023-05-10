def check(s):
    if s[0].isupper() and s[-1].isupper():
        if int(s[1:6]) >= 100000 and int(s[1:6]) <= 999999:
            return True
        else:
            return False
    else:
        return False
s = input()
print('Yes' if check(s) else 'No')
