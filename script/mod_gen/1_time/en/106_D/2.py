def main():
    N, M, Q = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    p = []
    q = []
    for i in range(Q):
        p_, q_ = map(int, input().split())
        p.append(p_)
        q.append(q_)
    #print(N, M, Q)
    #print(L)
    #print(R)
    #print(p)
    #print(q)
    for i in range(Q):
        count = 0
        for j in range(M):
            if L[j] >= p[i] and R[j] <= q[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()