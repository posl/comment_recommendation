def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        Ci, Ai = map(int, input().split())
        C.append(Ci)
        A.append(Ai)
    min_cost = -1
    for i in range(2**N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)
