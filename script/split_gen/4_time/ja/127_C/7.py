def solve():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[M-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[M-1] + 1)
