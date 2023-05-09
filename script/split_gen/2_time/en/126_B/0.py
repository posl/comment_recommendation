def main():
    S = input()
    if S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('NA')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        if int(S[2:4]) > 12:
            print('YYMM')
        else:
            print('AMBIGUOUS')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        if int(S[0:2]) > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')
    else:
        print('NA')
