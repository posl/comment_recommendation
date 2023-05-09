def main():
    s = input()
    if int(s[0:2]) <= 12 and int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    elif int(s[0:2]) <= 12:
        print('MMYY')
    elif int(s[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')
