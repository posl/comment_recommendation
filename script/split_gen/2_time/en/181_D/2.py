def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
    elif len(S) == 2:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(112, 1000, 8):
            if str(i).count('0') == 0 and str(i).count('1') == 0 and str(i).count('2') == 0:
                if str(i).count('3') <= S.count('3') and str(i).count('4') <= S.count('4') and str(i).count('5') <= S.count('5') and str(i).count('6') <= S.count('6') and str(i).count('7') <= S.count('7') and str(i).count('8') <= S.count('8') and str(i).count('9') <= S.count('9'):
                    print('Yes')
                    return
        print('No')
