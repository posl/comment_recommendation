def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        X[i] = A[i] if A[i] < B[i] else B[i]
    for i in range(N-1):
        if X[i+1] - X[i] > K:
            print('No')
            return
    print('Yes')
main()
