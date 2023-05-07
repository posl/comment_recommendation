def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    P, Q = zip(*PQ)
    P, Q = map(lambda x: [0] + list(x), [P, Q])
    # cumulative sum
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for L, R in LR:
        C[L][R] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            C[i][j] += C[i][j - 1]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            C[i][j] += C[i - 1][j]
    # query
    for i in range(1, Q + 1):
        print(C[Q[i]][Q[i]] - C[P[i] - 1][Q[i]] - C[Q[i]][P[i] - 1] + C[P[i] - 1][P[i] - 1])
