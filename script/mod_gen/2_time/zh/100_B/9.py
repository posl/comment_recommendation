def findNumber(D, N):
    if D == 0:
        if N == 100:
            return 101
        else:
            return N
    elif D == 1:
        if N == 100:
            return 10100
        else:
            return 100 * N
    else:
        if N == 100:
            return 1010000
        else:
            return 10000 * N

if __name__ == '__main__':
    findNumber()