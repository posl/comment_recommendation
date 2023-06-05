def solve():
    H, W, r, c = map(int, input().split())
    N = int(input())
    R = []
    C = []
    for i in range(N):
        r_, c_ = map(int, input().split())
        R.append(r_)
        C.append(c_)
    Q = int(input())
    D = []
    L = []
    for i in range(Q):
        d_, l_ = map(str, input().split())
        D.append(d_)
        L.append(l_)
    for i in range(Q):
        if D[i] == 'L':
            if c - int(L[i]) >= 1:
                c -= int(L[i])
        elif D[i] == 'R':
            if c + int(L[i]) <= W:
                c += int(L[i])
        elif D[i] == 'U':
            if r - int(L[i]) >= 1:
                r -= int(L[i])
        elif D[i] == 'D':
            if r + int(L[i]) <= H:
                r += int(L[i])
        print(r, c)

if __name__ == '__main__':
    solve()