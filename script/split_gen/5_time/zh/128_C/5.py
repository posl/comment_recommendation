def get_input():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
        s[i].sort()
    p = list(map(int, input().split()))
    return N, M, k, s, p
