def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = [S_1, S_2, S_3]
    S.sort()
    if S[0] == 'ABC':
        print('AGC')
    elif S[0] == 'ARC':
        print('AHC')
    elif S[0] == 'AGC':
        print('ABC')
    else:
        print('ARC')
