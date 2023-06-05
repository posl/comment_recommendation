def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        # X.sort()
        step = X[M-1] - X[0]
        for i in range(M-N+1):
            step = min(step, X[i+N-1] - X[i])
        print(step)
        return

if __name__ == '__main__':
    main()