def main():
    n = input()
    if 1 <= int(n[0:2]) <= 12:
        if 1 <= int(n[2:4]) <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif 1 <= int(n[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')
