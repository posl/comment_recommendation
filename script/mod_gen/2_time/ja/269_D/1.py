def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    print(N - len(set(X)) - len(set(Y)) + 1)

if __name__ == '__main__':
    main()