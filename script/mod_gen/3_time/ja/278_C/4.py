def init_par(n):
    par = {}
    for i in range(1, n + 1):
        par[i] = i
    return par

if __name__ == '__main__':
    init_par()