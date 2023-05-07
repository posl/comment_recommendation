def main():
    S = input()
    if S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('NA')
    elif S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S
