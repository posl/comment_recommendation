def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = T
    bonus = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        if i+1 in X:
            time += Y[X.index(i+1)]
        if time > T:
            time = T
    print("Yes")
    return

if __name__ == '__main__':
    main()