def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**10
    for i in range(2**N):
        t = [0]*(M+1)
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M+1):
                    t[k] += A[j][k]
        if all(t[k] >= X for k in range(1, M+1)):
            ans = min(ans, t[0])
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
