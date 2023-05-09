def solve():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(min(R) - max(L) + 1 if min(R) >= max(L) else 0)
