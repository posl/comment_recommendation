def solve():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    if s == t:
        if S == T:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
