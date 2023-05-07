def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
        s[i] = list(map(lambda x: x - 1, s[i]))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        on = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                on[j] = 1
        if all([sum([on[s[i][j]] for j in range(k[i])]) % 2 == p[i] for i in range(M)]):
            ans += 1
    print(ans)
