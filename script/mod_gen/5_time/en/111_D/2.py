def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    X = [x for x, y in XY]
    Y = [y for x, y in XY]
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if i == j == k:
                    continue
                if X[i] == X[j] == X[k] or Y[i] == Y[j] == Y[k]:
                    print(2)
                    print(1, 1)
                    print('LR')
                    print('UD')
                    return
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if i == j == k:
                    continue
                if X[i] == X[j] or Y[i] == Y[j]:
                    print(3)
                    print(1, 1, 1)
                    print('LRD')
                    print('UDU')
                    print('RDL')
                    return
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if i == j == k:
                    continue
                if X[i] == X[j] or Y[i] == Y[j]:
                    print(4)
                    print(1, 1, 1, 1)
                    print('LRDU')
                    print('UDUR')
                    print('RDUL')
                    print('DULR')
                    return
    print(5)
    print(1, 1, 1, 1, 1)
    print('LRDUL')
    print('UDULR')
    print('RDUUL')
    print('DULRD')
    print('ULRDU')
    return
main()

if __name__ == '__main__':
    main()