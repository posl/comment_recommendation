def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if B[L[i]-1] != 0:
            if B[L[i]-1] == N:
                pass
            elif B[L[i]] == 0:
                B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    for i in range(N):
        if B[i] != 0:
            print(B[i], end = " ")
