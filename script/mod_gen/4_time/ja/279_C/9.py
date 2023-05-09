def check(S, T):
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    check()