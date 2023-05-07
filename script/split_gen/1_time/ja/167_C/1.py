def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        tmp = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        if all([x >= X for x in tmp]):
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
