def main():
    # input
    Q = int(input())
    TXs = [list(map(int, input().split())) for _ in range(Q)]
    # compute
    A = [-1] * (2**20)
    for T, X in TXs:
        if T == 1:
            h = X
            while A[h%2**20] != -1:
                h += 1
            A[h%2**20] = X
        elif T == 2:
            print(A[X%2**20])
    # output

if __name__ == '__main__':
    main()