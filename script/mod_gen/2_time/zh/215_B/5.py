def calc_max_k(N):
    k = 0
    while True:
        if 2 ** k <= N:
            k += 1
        else:
            break
    return k - 1

if __name__ == '__main__':
    calc_max_k()