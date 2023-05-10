def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    M = max(T)
    A = [0] * (M + 1)
    for i in range(N):
        A[S[i]] += P[i]
        A[T[i]] -= P[i]
    for i in range(M):
        A[i + 1] += A[i]
        if A[i] > W:
            print('No')
            return
    print('Yes')
    return
