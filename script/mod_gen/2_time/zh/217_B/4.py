def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'AHC':
        print('ARC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('AGC')
    elif S[0] == 'AGC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('ABC')

if __name__ == '__main__':
    main()