def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0]*N
    for i in range(N):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(N):
        if i == 0:
            X[i] = A[i]
        else:
            if A[i] <= X[i-1] + K:
                X[i] = A[i]
            else:
                X[i] = B[i]
    for i in range(N-1):
        if abs(X[i] - X[i+1]) > K:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()