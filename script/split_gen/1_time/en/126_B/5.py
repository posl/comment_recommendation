def main():
    s = input()
    if (int(s[:2]) > 0 and int(s[:2]) < 13) and (int(s[2:]) > 0 and int(s[2:]) < 13):
        print('AMBIGUOUS')
    elif (int(s[:2]) > 0 and int(s[:2]) < 13):
        print('MMYY')
    elif (int(s[2:]) > 0 and int(s[2:]) < 13):
        print('YYMM')
    else:
        print('NA')
