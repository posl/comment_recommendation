def solve(n, m, t, ab):
    battery = n
    for i in range(m):
        if i == 0:
            battery -= ab[i][0]
        else:
            battery -= ab[i][0] - ab[i - 1][1]
        if battery <= 0:
            return False
        battery += ab[i][1] - ab[i][0]
        if battery > n:
            battery = n
    battery -= t - ab[m - 1][1]
    if battery <= 0:
        return False
    return True
