def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        L, R, X = query
        print(A[L-1:R].count(X))

if __name__ == '__main__':
    main()