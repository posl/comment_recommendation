def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    if N >= M:
        print(0)
    else:
        D = sorted([X[i+1] - X[i] for i in range(M-1)], reverse=True)
        print(sum(D[N-1:]))

if __name__ == '__main__':
    main()