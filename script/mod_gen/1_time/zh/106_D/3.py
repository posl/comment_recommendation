def get_input():
    n, m, q = map(int, raw_input().split())
    l = []
    r = []
    p = []
    q1 = []
    for i in range(m):
        l1, r1 = map(int, raw_input().split())
        l.append(l1)
        r.append(r1)
    for i in range(q):
        p1, q2 = map(int, raw_input().split())
        p.append(p1)
        q1.append(q2)
    return n, m, q, l, r, p, q1

if __name__ == '__main__':
    get_input()