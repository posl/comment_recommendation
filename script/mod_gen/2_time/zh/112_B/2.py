def solve(n, t, c, ti):
    cost = []
    for i in range(n):
        if ti[i] <= t:
            cost.append(c[i])
    if len(cost) == 0:
        return "TLE"
    else:
        return min(cost)

if __name__ == '__main__':
    solve()