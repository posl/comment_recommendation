def main():
    # input
    Q = int(input())
    Ts = []
    Xs = []
    for _ in range(Q):
        t, x = map(int, input().split())
        Ts.append(t)
        Xs.append(x)
    # compute
    N = 2**20
    As = [-1] * N
    for i in range(Q):
        if Ts[i] == 1:
            h = Xs[i]
            while As[h % N] != -1:
                h += 1
            As[h % N] = Xs[i]
        else:
            print(As[Xs[i] % N])
    # output

if __name__ == '__main__':
    main()