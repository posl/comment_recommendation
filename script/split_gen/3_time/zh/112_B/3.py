def searchBestRoute(N, T, c, t):
    if N <= 0:
        return 0
    if T <= 0:
        return 0
    if T < min(t):
        return 0
    if T == min(t):
        return min(c)
    if N == 1:
        return c[0]
    if N == 2:
        if T >= t[0] and T >= t[1]:
            return min(c)
        elif T >= t[0] and T < t[1]:
            return c[0]
        elif T >= t[1] and T < t[0]:
            return c[1]
        else:
            return 0
    if N > 2:
        if T >= t[0]:
            return min(c[0] + searchBestRoute(N - 1, T - t[0], c[1:], t[1:]),
                       searchBestRoute(N - 1, T, c[1:], t[1:]))
        else:
            return searchBestRoute(N - 1, T, c[1:], t[1:])
