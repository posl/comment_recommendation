def main():
    N, M, T = map(int, raw_input().split())
    A = map(int, raw_input().split())
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, raw_input().split())
        X.append(x)
        Y.append(y)
    X.append(0)
    Y.append(0)
    X.append(N)
    Y.append(0)
    X.sort()
    Y.sort()
    X.reverse()
    Y.reverse()
    time = T
    for i in range(N):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        time += Y[X.index(i+1)]
    print("Yes")

if __name__ == '__main__':
    main()