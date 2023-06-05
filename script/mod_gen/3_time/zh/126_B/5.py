def main():
    S = input()
    if (1 <= int(S[0:2]) <= 12) and (1 <= int(S[2:4]) <= 12):
        print('AMBIGUOUS')
    elif (1 <= int(S[0:2]) <= 12) and (1 <= int(S[2:4]) <= 99):
        print('MMYY')
    elif (1 <= int(S[0:2]) <= 99) and (1 <= int(S[2:4]) <= 12):
        print('YYMM')
    else:
        print('NA')

if __name__ == '__main__':
    main()