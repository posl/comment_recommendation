def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, L, R)
    # print(A)
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
    # print(A)
    sumA = sum(A)
    # print(sumA)
    for i in range(N):
        if A[i] < L:
            sumA += (L - A[i])
            A[i] = L
    # print(A)
    for i in range(N):
        if A[i] > R:
            sumA += (A[i] - R)
            A[i] = R
    # print(A)
    print(sumA)

if __name__ == '__main__':
    main()