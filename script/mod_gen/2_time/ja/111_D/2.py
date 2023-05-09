def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(0)
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(1)
            print(1)
            print('R')
            print('L')
        else:
            print(-1)
        return
    d = []
    for i in range(N - 1):
        d.append(abs(X[i] - X[i + 1]) + abs(Y[i] - Y[i + 1]))
    if d[0] != d[1] or d[1] != d[2]:
        print(-1)
        return
    m = 0
    for i in range(N - 1):
        m = max(m, abs(X[i] - X[i + 1]))
        m = max(m, abs(Y[i] - Y[i + 1]))
    print(m)
    print(*d)
    for i in range(N):
        s = ''
        for j in range(m):
            if X[i] > 0:
                X[i] -= 1
                s += 'R'
            elif X[i] < 0:
                X[i] += 1
                s += 'L'
            elif Y[i] > 0:
                Y[i] -= 1
                s += 'U'
            else:
                Y[i] += 1
                s += 'D'
        print(s)

if __name__ == '__main__':
    main()