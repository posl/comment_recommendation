def main():
    N, X, Y = map(int, input().split())
    tree = [[] for i in range(N+1)]
    for i in range(N-1):
        U, V = map(int, input().split())
        tree[U].append(V)
        tree[V].append(U)
    X_to_Y = [0 for i in range(N+1)]
    Y_to_X = [0 for i in range(N+1)]
    X_to_Y[X] = 1
    Y_to_X[Y] = 1
    for i in range(1,N+1):
        if X_to_Y[i] == 1:
            for j in tree[i]:
                if X_to_Y[j] == 0:
                    X_to_Y[j] = X_to_Y[i] + 1
        if Y_to_X[i] == 1:
            for j in tree[i]:
                if Y_to_X[j] == 0:
                    Y_to_X[j] = Y_to_X[i] + 1
    for i in range(1,N+1):
        if X_to_Y[i] == 0:
            X_to_Y[i] = N+1
        if Y_to_X[i] == 0:
            Y_to_X[i] = N+1
    for i in range(1,N+1):
        if X_to_Y[i] < Y_to_X[i]:
            print(i, end = " ")
    print(Y)
main()

if __name__ == '__main__':
    main()