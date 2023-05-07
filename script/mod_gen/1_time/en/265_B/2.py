def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0 for i in range(M)]
    Y = [0 for i in range(M)]
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = 0
    for i in range(N-1):
        time += A[i]
        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
        if time > T:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()