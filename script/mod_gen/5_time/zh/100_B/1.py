def getNthMinNum(D,N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    elif D == 2:
        return N * 10000

if __name__ == '__main__':
    getNthMinNum()