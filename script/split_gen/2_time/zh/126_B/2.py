def main():
    s = input()
    if s[0] == '0' and s[1] == '0':
        print('NA')
    elif s[0] == '0' and s[1] != '0':
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            print('YYMM')
        else:
            print('NA')
    elif s[0] != '0' and s[1] == '0':
        if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
            print('MMYY')
        else:
            print('NA')
    else:
        if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
            if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
                print('AMBIGUOUS')
            else:
                print('MMYY')
        else:
            if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
                print('YYMM')
            else:
                print('NA')
