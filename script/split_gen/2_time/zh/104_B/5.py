def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for c in s[1:]:
        if c != 'C' and c.isupper():
            return False
    return True
s = input()
print('AC' if check(s) else 'WA')
