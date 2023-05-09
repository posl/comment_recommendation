def main():
    S = input()
    a = int(S[0:2])
    b = int(S[2:4])
    if 1 <= a <= 12:
        if 1 <= b <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= b <= 12:
            print('YYMM')
        else:
            print('NA')

if __name__ == '__main__':
    main()