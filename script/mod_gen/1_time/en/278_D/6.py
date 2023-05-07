def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    X = []
    for query in queries:
        if query[0] == 1:
            A = [query[1]] * N
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        elif query[0] == 3:
            X.append(A[query[1] - 1])
    for x in X:
        print(x)

if __name__ == '__main__':
    main()