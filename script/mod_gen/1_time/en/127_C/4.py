def main():
    n, m = map(int, input().split())
    l = [0] * (m + 1)
    r = [0] * (m + 1)
    for i in range(1, m + 1):
        l[i], r[i] = map(int, input().split())
    lmax = l[1]
    rmin = r[1]
    for i in range(2, m + 1):
        lmax = max(lmax, l[i])
        rmin = min(rmin, r[i])
    print(max(0, rmin - lmax + 1))

if __name__ == '__main__':
    main()