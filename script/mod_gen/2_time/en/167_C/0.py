def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**10
    for i in range(2**N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j)&1 == 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()