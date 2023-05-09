def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for i in range(101):
        for j in range(101):
            H_max = 0
            for k in range(N):
                if H[k] != 0:
                    H_max = H[k] + abs(X[k] - i) + abs(Y[k] - j)
                    break
            if H_max == 0:
                H_max = 1
            for k in range(N):
                if H[k] != max(H_max - abs(X[k] - i) - abs(Y[k] - j), 0):
                    break
            else:
                print(i, j, H_max)
                return

if __name__ == '__main__':
    main()