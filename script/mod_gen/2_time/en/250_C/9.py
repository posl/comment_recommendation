def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    # print(N, Q)
    # print(X)
    # N = 10
    # Q = 6
    # X = [1, 5, 2, 9, 6, 6]
    # print(N, Q)
    # print(X)
    # N = 7
    # Q = 7
    # X = [7, 7, 7, 7, 7, 7, 7]
    # print(N, Q)
    # print(X)
    # N = 5
    # Q = 5
    # X = [1, 2, 3, 4, 5]
    # print(N, Q)
    # print(X)
    A = list(range(1, N + 1))
    # print(A)
    for x in X:
        index = A.index(x)
        # print("index:", index)
        if index == N - 1:
            A[index], A[0] = A[0], A[index]
        else:
            A[index], A[index + 1] = A[index + 1], A[index]
        # print(A)
    print(*A)

if __name__ == '__main__':
    main()