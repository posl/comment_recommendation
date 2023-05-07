def get_input():
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
        pi, qi = map(int, input().split())
        p.append(pi)
        q.append(qi)
    return N, M, Q, L, R, p, q

if __name__ == '__main__':
    get_input()