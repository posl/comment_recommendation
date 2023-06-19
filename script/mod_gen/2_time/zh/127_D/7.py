def solve(n, m, a, bc):
    a.sort(reverse=True)
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] >= bc[j][1]:
            i += 1
        else:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
            i += 1
    return sum(a)

if __name__ == '__main__':
    solve()