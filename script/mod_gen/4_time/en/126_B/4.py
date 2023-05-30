def check(s):
    if (s[0] == '0' and s[1] == '0') or (s[2] == '0' and s[3] == '0'):
        return 'NA'
    elif (s[0] == '0' or s[0] == '1') and (s[2] == '0' or s[2] == '1'):
        return 'AMBIGUOUS'
    elif s[0] == '0' or s[0] == '1':
        return 'YYMM'
    elif s[2] == '0' or s[2] == '1':
        return 'MMYY'
    else:
        return 'NA'
s = input()
print(check(s))
