def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) > 0 and int(s1) < 13:
        if int(s2) > 0 and int(s2) < 13:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif int(s2) > 0 and int(s2) < 13:
        print('YYMM')
    else:
        print('NA')
