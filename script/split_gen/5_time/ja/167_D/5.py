def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - 1
    C = [0] * N
    C[0] = 1
    D = [0] * N
    D[0] = 0
    p = 0
    for i in range(1, N + 1):
        p = B[p]
        if C[p] == 1:
            break
        C[p] = 1
        D[p] = i
    if i == N:
        print(B[p] + 1)
    else:
        n = i - D[p]
        K = (K - D[p]) % n
        for i in range(K):
            p = B[p]
        print(p + 1)
