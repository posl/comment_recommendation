def main():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12 and (b == 0 or b > 12):
        print('MMYY')
    elif 1 <= b <= 12 and (a == 0 or a > 12):
        print('YYMM')
    else:
        print('NA')
