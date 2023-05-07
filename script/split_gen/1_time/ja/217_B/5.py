def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC':
        print('ARC')
    elif S[0] == 'AGC':
        print('AHC')
    elif S[0] == 'ARC':
        print('AGC')
