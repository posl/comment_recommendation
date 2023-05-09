def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    ans = 10**9 + 1
    for i in range(2**N):
        cost = 0
        tmp = [0 for i in range(M)]
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        for j in range(M):
            if tmp[j] < X:
                break
        else:
            ans = min(ans, cost)
    print(-1 if ans == 10**9 + 1 else ans)
