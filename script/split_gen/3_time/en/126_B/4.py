def main():
    s = input()
    yy = int(s[0:2])
    mm = int(s[2:4])
    if 1 <= mm <= 12:
        if 1 <= yy <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= yy <= 12:
            print('YYMM')
        else:
            print('NA')
