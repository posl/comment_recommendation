def check():
    #input
    D, T, S = map(int, input().split())
    #calc
    if D/S <= T:
        print('Yes')
    else:
        print('No')
