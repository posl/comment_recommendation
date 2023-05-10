def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        x = list(map(int, input().split()))
        C.append(x[0])
        A.append(x[1:])
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        understanding_level = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    understanding_level[k] += A[j][k]
        if min(understanding_level) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()