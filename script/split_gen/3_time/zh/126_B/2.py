def main():
    S = input()
    S1 = int(S[:2])
    S2 = int(S[2:])
    if S1 in range(1, 13) and S2 in range(1, 13):
        print('AMBIGUOUS')
    elif S1 in range(1, 13):
        print('MMYY')
    elif S2 in range(1, 13):
        print('YYMM')
    else:
        print('NA')
