def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    friend = [0] * N
    for i in range(M):
        friend[A[i] - 1] += 1
        friend[B[i] - 1] += 1
    block = [0] * N
    for i in range(K):
        block[C[i] - 1] += 1
        block[D[i] - 1] += 1
    for i in range(N):
        print(friend[i] - block[i] - 1, end=' ')
