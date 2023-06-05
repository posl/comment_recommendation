def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.sort()
    X = [x for x, _ in XY]
    Y = [y for _, y in XY]
    if N == 1:
        print(-1)
        return
    if N == 2:
        if X[0] == X[1] or Y[0] == Y[1]:
            print(-1)
            return
        print(2)
        print(1, 1)
        print('RL')
        print('UD')
        return
    for i in range(N - 1):
        if X[i] == X[i + 1] or Y[i] == Y[i + 1]:
            print(-1)
            return
    print(N + 1)
    print(1, 1, 4, 1, 5)
    print('R' * (N - 2) + 'LU')
    print('R' * (N - 2) + 'LD')
    print('L' * (N - 2) + 'RU')
    print('L' * (N - 2) + 'RD')
    print('U' * (N - 2) + 'RD')
    print('U' * (N - 2) + 'LD')
    print('D' * (N - 2) + 'RU')
    print('D' * (N - 2) + 'LU')

if __name__ == '__main__':
    main()