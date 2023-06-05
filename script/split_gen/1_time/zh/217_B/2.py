def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'AHC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
        print('ARC')
        print('AGC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('AGC')
        print('ARC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AGC':
        print('AHC')
        print('AGC')
        print('ARC')
    elif S[0] == 'ABC' and S[1] == 'AHC' and S[2] == 'AGC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AHC' and S[2] == 'ARC':
        print('AGC')
        print('ARC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'AHC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'ARC':
        print('AHC')
        print('ARC')
        print('AGC')
    elif S[0] == 'AGC' and S[1] == 'AHC' and S[2] == 'ABC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'AHC' and S[2] == 'ARC':
        print('ABC')
        print('ARC')
        print('AGC
