def main():
    N, M = map(int, input().split())
    X = [0 for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        X[a-1] += 1
        X[b-1] += 1
    print(max(X))

if __name__ == '__main__':
    main()