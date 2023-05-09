def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    dist = []
    for i in range(M - 1):
        dist.append(X[i + 1] - X[i])
    dist.sort(reverse=True)
    print(sum(dist[N - 1:]))

if __name__ == '__main__':
    main()