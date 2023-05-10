def main():
    s = input()
    a = int(s[0:2])
    b = int(s[2:4])
    if a == 0 and b == 0:
        print('NA')
    elif a == 0 and b != 0:
        print('YYMM')
    elif a != 0 and b == 0:
        print('MMYY')
    elif 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12 and not(1 <= b <= 12):
        print('MMYY')
    elif not(1 <= a <= 12) and 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')
