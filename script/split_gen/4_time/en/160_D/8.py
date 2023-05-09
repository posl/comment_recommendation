def calc_dist(n, x, y):
    dist = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            dist[min(abs(i - j), abs(i - x) + 1 + abs(j - y), abs(i - y) + 1 + abs(j - x))] += 1
    return dist[1:]
