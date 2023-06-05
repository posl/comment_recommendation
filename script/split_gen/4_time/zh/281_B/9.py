def check():
    S = input()
    if S[0] < 'A' or S[0] > 'Z':
        print('No')
        return
    if S[-1] < 'A' or S[-1] > 'Z':
        print('No')
        return
    if len(S) != 8:
        print('No')
        return
    if S[1] < '0' or S[1] > '9':
        print('No')
        return
    if S[2] < '0' or S[2] > '9':
        print('No')
        return
    if S[3] < '0' or S[3] > '9':
        print('No')
        return
    if S[4] < '0' or S[4] > '9':
        print('No')
        return
    if S[5] < '0' or S[5] > '9':
        print('No')
        return
    if S[6] < '0' or S[6] > '9':
        print('No')
        return
    if S[1] != '0':
        print('No')
        return
    if S[2] != '0':
        print('No')
        return
    if S[3] != '0':
        print('No')
        return
    if S[4] != '0':
        print('No')
        return
    if S[5] != '0':
        print('No')
        return
    if S[6] != '0':
        print('No')
        return
    if int(S[1:7]) < 100000:
        print('No')
        return
    if int(S[1:7]) > 999999:
        print('No')
        return
    print('Yes')
    return
