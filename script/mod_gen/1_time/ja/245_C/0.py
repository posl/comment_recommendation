def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    X[0] = A[0]
    for i in range(1, N):
        if abs(A[i] - X[i-1]) <= K and abs(B[i] - X[i-1]) <= K:
            X[i] = min(A[i], B[i])
        elif abs(A[i] - X[i-1]) <= K:
            X[i] = A[i]
        elif abs(B[i] - X[i-1]) <= K:
            X[i] = B[i]
        else:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()