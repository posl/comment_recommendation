def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        if (i+1) in X:
            time += Y[X.index(i+1)]
            if time > T:
                time = T
    print("Yes")

if __name__ == '__main__':
    main()