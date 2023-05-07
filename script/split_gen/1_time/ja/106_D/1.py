def main():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(Q):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)
    for i in range(Q):
        ans = 0
        for j in range(M):
            if P[i] <= L[j] and R[j] <= Q[i]:
                ans += 1
        print(ans)
