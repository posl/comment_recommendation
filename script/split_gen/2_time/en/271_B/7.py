def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    L = [0] * N
    A = []
    for i in range(N):
        L[i] = int(input())
        A.append(list(map(int, input().split())))
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    #print(N, Q)
    #print(L)
    #print(A)
    #print(S)
    #print(T)
    # L[i] = len(A[i])
    # A[i][j] = i-th sequence, j-th term
    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}
    # S[k] = s_k
    # T[k] = t_k
    # S = [S[0], S[1], ..., S[Q-1]]
    # T = [T[0], T[1], ..., T[Q-1]]
    # A[i][j] = i-th sequence, j-th term
    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}
    # S[k] = s_k
    # T[k] = t_k
    # S = [S[0], S[1], ..., S[Q-1]]
    # T = [T[0], T[1], ..., T[Q-1]]
    # A[i][j] = i-th sequence, j-th term
    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}
    # S[k] =
