def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    Lmax = max(L)
    Rmin = min(R)
    if Rmin - Lmax + 1 >= 0:
        print(Rmin - Lmax + 1)
    else:
        print(0)
