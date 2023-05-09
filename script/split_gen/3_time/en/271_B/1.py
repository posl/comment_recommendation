def main():
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i] = list(map(int, input().split()))
        A[i] = L[i][1:]
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    for i in range(Q):
        print(A[S[i] - 1][T[i] - 1])
