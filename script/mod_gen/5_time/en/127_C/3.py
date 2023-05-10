def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L_max = max(L)
    R_min = min(R)
    if R_min < L_max:
        print(0)
    else:
        print(R_min - L_max + 1)

if __name__ == '__main__':
    solve()