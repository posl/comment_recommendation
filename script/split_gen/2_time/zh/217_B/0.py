def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S == ['ABC', 'AGC', 'ARC']:
        print('AHC')
    elif S == ['ABC', 'AGC', 'AHC']:
        print('ARC')
    elif S == ['ABC', 'ARC', 'AHC']:
        print('AGC')
    elif S == ['AGC', 'ARC', 'AHC']:
        print('ABC')
