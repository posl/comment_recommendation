def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i]
    B.sort()
    for i in range(N):
        if A[i] != B[i]:
            if (i + K) > N:
                print('No')
                return
            else:
                for j in range(K):
                    A[i + j], A[i + j + 1] = A[i + j + 1], A[i + j]
    for i in range(N):
        if A[i] != B[i]:
            print('No')
            return
    print('Yes')
