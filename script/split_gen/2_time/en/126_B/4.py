def main():
    s = input()
    month = int(s[2:4])
    year = int(s[0:2])
    if (0 < month < 13) and (0 < year < 13):
        print('AMBIGUOUS')
    elif 0 < month < 13:
        print('MMYY')
    elif 0 < year < 13:
        print('YYMM')
    else:
        print('NA')
