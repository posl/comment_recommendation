def get_max_blue_jewels(N, X, Y):
    if N == 1:
        return 0
    if X == 1 and Y == 1:
        return (N - 1) * 2
    if X == 1:
        return (N - 1) * 2 * Y
    if Y == 1:
        return (N - 1) * 2 * X
    return (N - 1) * 2 * X * Y
