def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    X = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(N):
                A[j] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        elif query[0] == 3:
            X.append(A[query[1]-1])
    for i in range(len(X)):
        print(X[i])

if __name__ == '__main__':
    main()