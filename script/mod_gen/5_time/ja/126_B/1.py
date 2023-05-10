def main():
    S = input()
    S1 = int(S[0:2])
    S2 = int(S[2:4])
    if S1 >= 1 and S1 <= 12 and S2 >= 1 and S2 <= 12:
        print('AMBIGUOUS')
    elif S1 >= 1 and S1 <= 12:
        print('MMYY')
    elif S2 >= 1 and S2 <= 12:
        print('YYMM')
    else:
        print('NA')

if __name__ == '__main__':
    main()