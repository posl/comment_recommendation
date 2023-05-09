def main():
    # read input
    N, M, Q = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(M)]
    PQ = [tuple(map(int, input().split())) for _ in range(Q)]
    # create cumulative sum
    cumsum = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in LR:
        cumsum[l][r] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cumsum[i][j] += cumsum[i - 1][j] + cumsum[i][j - 1] - cumsum[i - 1][j - 1]
    # output
    for p, q in PQ:
        print(cumsum[q][q] - cumsum[p - 1][q] - cumsum[q][p - 1] + cumsum[p - 1][p - 1])
