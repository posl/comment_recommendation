def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                understanding = [understanding[k] + A[j][k] for k in range(M)]
        if all([understanding[k] >= X for k in range(M)]):
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    print(min_cost)

if __name__ == '__main__':
    main()