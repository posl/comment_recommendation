def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        on = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    if j+1 in S[k][1:]:
                        on[k] += 1
        if all([on[k]%2 == P[k] for k in range(M)]):
            ans += 1
    print(ans)
