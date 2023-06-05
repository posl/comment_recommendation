def solve(n, m, p, s):
    ac = 0
    wa = 0
    acs = [0] * n
    was = [0] * n
    for i in range(m):
        if s[i] == "AC":
            if acs[p[i]-1] == 0:
                ac += 1
                acs[p[i]-1] = 1
                wa += was[p[i]-1]
        else:
            if acs[p[i]-1] == 0:
                was[p[i]-1] += 1
    return ac, wa

if __name__ == '__main__':
    solve()