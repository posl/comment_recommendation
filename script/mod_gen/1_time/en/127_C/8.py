def main():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    lmax = max(L)
    rmin = min(R)
    if lmax <= rmin:
        print(rmin-lmax+1)
    else:
        print(0)

if __name__ == '__main__':
    main()