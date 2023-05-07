def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            X[i] = max(A[i], B[i])
        else:
            X[i] = min(A[i], B[i])
            if abs(A[i] - B[i]) > K:
                print('No')
                return
    for i in range(N - 1):
        if abs(X[i] - X[i + 1]) > K:
            print('No')
            return
    print('Yes')
