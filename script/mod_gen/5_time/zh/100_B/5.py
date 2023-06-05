def get_num(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    else:
        return N * 10000

if __name__ == '__main__':
    get_num()