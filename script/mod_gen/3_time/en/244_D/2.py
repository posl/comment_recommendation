def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()
    S = S1+S2+S3
    T = T1+T2+T3
    if S == 'RGB' and T == 'RGB':
        print('Yes')
    elif S == 'RGB' and T == 'RBG':
        print('Yes')
    elif S == 'RBG' and T == 'RGB':
        print('Yes')
    elif S == 'RBG' and T == 'BGR':
        print('Yes')
    elif S == 'BGR' and T == 'RBG':
        print('Yes')
    elif S == 'BGR' and T == 'BRG':
        print('Yes')
    elif S == 'BRG' and T == 'BGR':
        print('Yes')
    elif S == 'BRG' and T == 'GRB':
        print('Yes')
    elif S == 'GRB' and T == 'BRG':
        print('Yes')
    elif S == 'GRB' and T == 'GBR':
        print('Yes')
    elif S == 'GBR' and T == 'GRB':
        print('Yes')
    elif S == 'GBR' and T == 'RGB':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()