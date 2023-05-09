def main():
    S = input()
    if int(S[:2]) in range(1,13) and int(S[2:]) in range(1,13):
        print('AMBIGUOUS')
    elif int(S[:2]) in range(1,13):
        print('MMYY')
    elif int(S[2:]) in range(1,13):
        print('YYMM')
    else:
        print('NA')
