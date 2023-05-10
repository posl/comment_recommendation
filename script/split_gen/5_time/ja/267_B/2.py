def solve():
    S = input()
    if S[0] == '0':
        print('No')
        return
    if S[9] == '0':
        print('No')
        return
    if S[1] == '0' and S[2] == '0':
        print('No')
        return
    if S[8] == '0' and S[7] == '0':
        print('No')
        return
    if S[1] == '0' and S[8] == '0':
        print('No')
        return
    print('Yes')
    return
