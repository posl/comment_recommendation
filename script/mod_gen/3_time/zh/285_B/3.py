def get_max_l(S, i):
    N = len(S)
    l = 0
    while l + i < N:
        if S[l] != S[l + i]:
            l += 1
        else:
            break
    return l

if __name__ == '__main__':
    get_max_l()