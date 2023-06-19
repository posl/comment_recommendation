def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if 1 <= int(S1) <= 12:
        if 1 <= int(S2) <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= int(S2) <= 12:
            print('YYMM')
        else:
            print('NA')

if __name__ == '__main__':
    main()