def problem126_b():
    s = input()
    if 1 <= int(s[0:2]) <= 12:
        if 1 <= int(s[2:4]) <= 12:
            print('AMBIGUOUS')
            return
        else:
            print('MMYY')
            return
    elif 1 <= int(s[2:4]) <= 12:
        print('YYMM')
        return
    else:
        print('NA')
        return
problem126_b()
