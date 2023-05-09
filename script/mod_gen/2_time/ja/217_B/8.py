def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'AGC' and S[1] == 'ARC' and S[2] == 'ABC':
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ARC' and S[1] == 'AGC' and S[2] == 'ABC':
        print('AHC')
    elif S[0] == 'ARC' and S[1] == 'ABC' and S[2] == 'AGC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AGC':
        print('AHC')
    else:
        print(S[0])

if __name__ == '__main__':
    main()