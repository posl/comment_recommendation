def main():
    s = input()
    m1 = int(s[0:2])
    m2 = int(s[2:4])
    if 1 <= m1 <= 12 and 1 <= m2 <= 12:
        print('AMBIGUOUS')
    elif 1 <= m1 <= 12:
        print('MMYY')
    elif 1 <= m2 <= 12:
        print('YYMM')
    else:
        print('NA')
