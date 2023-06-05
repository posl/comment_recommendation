def main():
    s = input()
    s1 = s[:2]
    s2 = s[2:]
    if s1[0] == '0' and s1[1] == '0':
        if s2[0] == '0' and s2[1] == '0':
            print('NA')
        else:
            print('MMYY')
    elif s2[0] == '0' and s2[1] == '0':
        if s1[0] == '0' and s1[1] == '0':
            print('NA')
        else:
            print('YYMM')
    elif s1[0] == '0' and s1[1] != '0':
        if s2[0] == '0' and s2[1] != '0':
            print('NA')
        else:
            print('MMYY')
    elif s2[0] == '0' and s2[1] != '0':
        if s1[0] == '0' and s1[1] != '0':
            print('NA')
        else:
            print('YYMM')
    else:
        print('AMBIGUOUS')
