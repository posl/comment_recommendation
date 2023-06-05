def main():
    S = input()
    m1 = int(S[0:2])
    m2 = int(S[2:4])
    if m1 < 1 or m1 > 12:
        if m2 < 1 or m2 > 12:
            print('NA')
        else:
            print('YYMM')
    else:
        if m2 < 1 or m2 > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')

if __name__ == '__main__':
    main()