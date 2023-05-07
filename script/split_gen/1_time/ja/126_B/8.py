def main():
    s = input()
    # YYMM
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    # YYMM
    elif 1 <= int(s[0:2]) <= 12:
        print('YYMM')
    # MMYY
    elif 1 <= int(s[2:4]) <= 12:
        print('MMYY')
    # NA
    else:
        print('NA')
