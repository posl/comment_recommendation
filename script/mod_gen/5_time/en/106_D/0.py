def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    trains = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        L = LR[i][0] - 1
        R = LR[i][1] - 1
        for j in range(L, R + 1):
            trains[j][i] = 1
    trains = [[sum(row[:i]) for i in range(M + 1)] for row in trains]
    for i in range(Q):
        P = PQ[i][0] - 1
        Q = PQ[i][1] - 1
        print(sum([trains[j][Q] - trains[j][P] for j in range(P, Q + 1)]))

if __name__ == '__main__':
    main()