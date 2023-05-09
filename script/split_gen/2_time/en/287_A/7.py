def check_majority():
    N = int(input())
    if N%2 != 0:
        S = []
        for i in range(N):
            S.append(input())
        if S.count('For') > S.count('Against'):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
