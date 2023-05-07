def main():
    S = input()
    if S[0:2] >= '01' and S[0:2] <= '12':
        if S[2:4] >= '01' and S[2:4] <= '12':
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if S[2:4] >= '01' and S[2:4] <= '12':
            print('YYMM')
        else:
            print('NA')
