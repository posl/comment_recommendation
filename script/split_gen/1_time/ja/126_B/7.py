def main():
    S = input()
    YYMM = False
    MMYY = False
    if S[0] == '0' or S[0] == '1':
        if S[1] == '0' or S[1] == '1' or S[1] == '2':
            YYMM = True
    if S[2] == '0' or S[2] == '1':
        if S[3] == '0' or S[3] == '1' or S[3] == '2' or S[3] == '3':
            MMYY = True
    if YYMM and MMYY:
        print('AMBIGUOUS')
    elif YYMM:
        print('YYMM')
    elif MMYY:
        print('MMYY')
    else:
        print('NA')
