def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    total_cost = float('inf')
    for i in range(1 << N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i >> j & 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all(x >= X for x in understanding):
            total_cost = min(total_cost, cost)
    if total_cost == float('inf'):
        print(-1)
    else:
        print(total_cost)
