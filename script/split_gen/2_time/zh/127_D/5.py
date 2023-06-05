def main():
    n, m = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    lmax = max(l)
    rmin = min(r)
    print(max(0, rmin - lmax + 1))
