def main():
    s = input()
    y1 = int(s[:2])
    y2 = int(s[2:])
    if y1 >= 1 and y1 <= 12 and y2 >= 1 and y2 <= 12:
        print('AMBIGUOUS')
    elif y1 >= 1 and y1 <= 12:
        print('MMYY')
    elif y2 >= 1 and y2 <= 12:
        print('YYMM')
    else:
        print('NA')
