def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        C.append(list(map(int, input().split())))
    for i in range(N):
        A.append(C[i][1:])
        C[i] = C[i][0]
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understand = [0 for i in range(M)]
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

if __name__ == '__main__':
    main()