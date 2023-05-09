def main():
    S = input()
    Y = int(S[0:2])
    M = int(S[2:4])
    if Y >= 1 and Y <= 12 and M >= 1 and M <= 12:
        print('AMBIGUOUS')
    elif Y >= 1 and Y <= 12:
        print('YYMM')
    elif M >= 1 and M <= 12:
        print('MMYY')
    else:
        print('NA')

if __name__ == '__main__':
    main()