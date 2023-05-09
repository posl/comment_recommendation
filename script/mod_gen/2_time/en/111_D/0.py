def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(2)
        print(1, 1)
        print('RU')
        print('UR')
        return
    for i in range(N):
        for j in range(i+1, N):
            if X[i] == X[j] and Y[i] == Y[j]:
                print(-1)
                return
    m = 1
    d = [1]
    w = ['U'] * N
    for i in range(N):
        if abs(X[i]) + abs(Y[i]) > d[0]:
            d[0] = abs(X[i]) + abs(Y[i])
    while True:
        for i in range(N):
            if X[i] < 0:
                w[i] = 'L' + w[i]
                X[i] += d[m-1]
            elif X[i] > 0:
                w[i] = 'R' + w[i]
                X[i] -= d[m-1]
            elif Y[i] < 0:
                w[i] = 'D' + w[i]
                Y[i] += d[m-1]
            elif Y[i] > 0:
                w[i] = 'U' + w[i]
                Y[i] -= d[m-1]
        flag = True
        for i in range(N):
            if X[i] != 0 or Y[i] != 0:
                flag = False
                break
        if flag:
            break
        m += 1
        d.append(1)
        for i in range(N):
            if abs(X[i]) + abs(Y[i]) > d[m-1]:
                d[m-1] = abs(X[i]) + abs(Y[i])
    print(m)
    print(*d)
    for i in range(N):
        print(w[i])
main()
The code is written in Python 3.4.3.
The code is written in Python 3.4.3.

if __name__ == '__main__':
    main()