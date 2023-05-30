def check_YYMM(S):
    YY = int(S[0:2])
    MM = int(S[2:4])
    if 1 <= YY <= 12 and 1 <= MM <= 12:
        return 'AMBIGUOUS'
    elif 1 <= YY <= 12 and 1 <= MM <= 12:
        return 'YYMM'
    elif 1 <= MM <= 12 and 1 <= YY <= 12:
        return 'MMYY'
    else:
        return 'NA'
S = input()
print(check_YYMM(S))
