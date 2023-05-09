def solve():
    n, m = map(int, input().split())
    ps = []
    for i in range(m):
        p, s = input().split()
        ps.append((int(p), s))
    acs = [0] * n
    was = [0] * n
    for p, s in ps:
        p -= 1
        if s == 'AC':
            acs[p] = 1
        elif acs[p] == 0:
            was[p] += 1
    ac = sum(acs)
    wa = 0
    for i in range(n):
        if acs[i] == 1:
            wa += was[i]
    print(ac, wa)
