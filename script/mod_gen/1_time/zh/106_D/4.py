def main():
    n, m, q = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    p = []
    q = []
    for i in range(q):
        p_, q_ = map(int, input().split())
        p.append(p_)
        q.append(q_)
    for i in range(q):
        count = 0
        for j in range(m):
            if l[j] >= p[i] and r[j] <= q[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()