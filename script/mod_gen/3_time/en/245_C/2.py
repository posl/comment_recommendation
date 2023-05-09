def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if A[i] == B[i]:
            X[i] = A[i]
        else:
            X[i] = max(A[i], B[i])
    for i in range(N - 1):
        if abs(X[i] - X[i + 1]) > K:
            print("No")
            return
    print("Yes")
main()

if __name__ == '__main__':
    main()