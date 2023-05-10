def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**10
    for i in range(1<<N):
        cost = 0
        skill = [0] * M
        for j in range(N):
            if i & (1<<j):
                cost += C[j]
                for k in range(M):
                    skill[k] += A[j][k]
        if min(skill) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**10:
        print(-1)
    else:
        print(min_cost)
