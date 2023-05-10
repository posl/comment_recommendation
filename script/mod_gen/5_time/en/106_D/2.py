def main():
    N, M, Q = map(int, input().split())
    L, R = [], []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    P, Q = [], []
    for i in range(Q):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)
    ans = []
    for i in range(Q):
        ans.append(sum([1 for i in range(M) if P[i] <= L[i] and R[i] <= Q[i]]))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()