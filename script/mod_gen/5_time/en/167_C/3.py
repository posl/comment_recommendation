def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    result = 10**6
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all([x>=X for x in understanding]):
            result = min(result, cost)
    if result == 10**6:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    main()