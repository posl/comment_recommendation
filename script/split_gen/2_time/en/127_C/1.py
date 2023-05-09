def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    Lmax = max(L)
    Rmin = min(R)
    if Lmax > Rmin:
        print(0)
    else:
        print(Rmin - Lmax + 1)
