def f(N, M, L):
    if N == 0:
        print(*L)
        return
    for i in range(1, M+1):
        if L and L[-1] >= i:
            continue
        f(N-1, M, L+[i])
N, M = map(int, input().split())
f(N, M, [])
