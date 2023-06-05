def fun():
    n,m,q = map(int, input().split())
    L = []
    R = []
    for i in range(m):
        l,r = map(int, input().split())
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for i in range(q):
        p,q = map(int, input().split())
        P.append(p)
        Q.append(q)
    for i in range(q):
        count = 0
        for j in range(m):
            if P[i] <= L[j] and R[j] <= Q[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    fun()