def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #print(B)
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            return False
    X = [0] * N
    for i in range(N):
        X[i] = min(A[i], B[i]) + K
    for i in range(N-1):
        if X[i] - X[i+1] > K:
            return False
    return True

if __name__ == '__main__':
    solve()