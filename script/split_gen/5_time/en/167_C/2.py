def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**9
    for i in range(2**N):
        sum_cost = 0
        sum_A = [0]*M
        for j in range(N):
            if i>>j & 1:
                sum_cost += C[j]
                for k in range(M):
                    sum_A[k] += A[j][k]
        if all([a>=X for a in sum_A]):
            min_cost = min(min_cost, sum_cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)
