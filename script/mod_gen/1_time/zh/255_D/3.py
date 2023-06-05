def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # print(N, Q, A, X)
    for i in range(Q):
        # print(i, X[i])
        # print(A)
        for j in range(N):
            # print(j, A[j])
            if A[j] > X[i]:
                A[j] = X[i]
        # print(A)
        print(sum(A))

if __name__ == '__main__':
    main()