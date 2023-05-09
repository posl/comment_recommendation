def main():
    N, Q = map(int, input().split())
    L = [0 for i in range(N)]
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
        L[i] = A[i][0]
    S = [0 for i in range(Q)]
    T = [0 for i in range(Q)]
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    for i in range(Q):
        print(A[S[i] - 1][T[i]])
