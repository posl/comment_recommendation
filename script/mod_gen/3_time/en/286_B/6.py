def f(N,S):
    if N < 2:
        return S
    elif N == 2:
        if S == 'na':
            return 'nya'
        else:
            return S
    else:
        if S[0:2] == 'na':
            return 'nya' + f(N-2, S[2:])
        else:
            return S[0] + f(N-1, S[1:])

if __name__ == '__main__':
    f()