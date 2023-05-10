def problems167_a():
    S = input()
    T = input()
    if len(S) == len(T)-1 and S == T[:-1]:
        print('Yes')
    else:
        print('No')
problems167_a()
