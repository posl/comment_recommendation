def problem100_b(D,N):
    if D == 0:
        if N == 100:
            return 101
        else:
            return 100**D * N
    elif D == 1:
        if N == 100:
            return 10001
        else:
            return 100**D * N
    else:
        if N == 100:
            return 1000001
        else:
            return 100**D * N

if __name__ == '__main__':
    problem100_b()