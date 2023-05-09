def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        alg = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    alg[k] += A[j][k]
        for k in range(M):
            if alg[k] < X:
                break
        else:
            ans = min(ans, cost)
    print(ans if ans != 10**9 else -1)
