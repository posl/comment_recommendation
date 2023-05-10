def replace(s):
    i = 0
    r = ''
    while i < len(s):
        if s[i] == 'A':
            r = r + 'BC'
        elif s[i] == 'B':
            r = r + 'CA'
        else:
            r = r + 'AB'
        i = i + 1
    return r
s = input()
q = int(input())
