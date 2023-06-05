def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(j) for j in input().split()])
    for query in queries:
        if query[0] == 1:
            for i in range(N):
                A[i] = query[1]
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        else:
            print(A[query[1] - 1])

if __name__ == '__main__':
    main()