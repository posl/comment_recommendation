def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(x) for x in input().split()])
    A = [0] + A
    for i in range(1, N+1):
        A[i] = A[i-1] + A[i]
    for query in queries:
        L, R, X = query
        print(A[R] - A[L-1] - (R - L + 1) * X)

if __name__ == '__main__':
    main()