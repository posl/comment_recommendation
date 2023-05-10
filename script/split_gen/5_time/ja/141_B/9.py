def solve():
    S = input()
    for i in range(len(S)):
        if (i+1) % 2 == 0:
            if S[i] in ['L','U','D']:
                pass
            else:
                print('No')
                return
        else:
            if S[i] in ['R','U','D']:
                pass
            else:
                print('No')
                return
    print('Yes')
    return
