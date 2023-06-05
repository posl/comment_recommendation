def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    R = []
    C = []
    for i in range(N):
        r, c = map(int, input().split())
        R.append(r)
        C.append(c)
    Q = int(input())
    D = []
    L = []
    for i in range(Q):
        d, l = input().split()
        D.append(d)
        L.append(l)
    print(H, W, rs, cs)
    print(N)
    for i in range(N):
        print(R[i], C[i])
    print(Q)
    for i in range(Q):
        print(D[i], L[i])

if __name__ == '__main__':
    main()