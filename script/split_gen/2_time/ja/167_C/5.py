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
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += C[j]
        if sum >= ans:
            continue
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = sum
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
