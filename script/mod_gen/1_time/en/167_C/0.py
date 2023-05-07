def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**6
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i>>j & 1:
                cost += C[j]
                understanding = [x+y for x,y in zip(understanding, A[j])]
        if all(x >= X for x in understanding):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost != 10**6 else -1)

if __name__ == '__main__':
    main()