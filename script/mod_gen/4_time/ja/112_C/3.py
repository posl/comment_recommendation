def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H0 = 0
            for i in range(N):
                if H[i] != 0:
                    H0 = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
                    break
            for i in range(N):
                if max(H0 - abs(X[i] - cx) - abs(Y[i] - cy), 0) != H[i]:
                    break
            else:
                print(cx, cy, H0)
                return

if __name__ == '__main__':
    main()