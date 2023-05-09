def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        X_i, Y_i = map(int, input().split())
        X.append(X_i)
        Y.append(Y_i)
    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            exit()
        if room in X:
            time += Y[X.index(room)]
        room += 1
    print("Yes")

if __name__ == '__main__':
    main()