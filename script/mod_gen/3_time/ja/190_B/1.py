def main():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()