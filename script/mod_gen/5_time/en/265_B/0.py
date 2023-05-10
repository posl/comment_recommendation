def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if i+1 in X:
            t += Y[X.index(i+1)]
            if t > T:
                t = T
    print("Yes")
    return

if __name__ == '__main__':
    main()