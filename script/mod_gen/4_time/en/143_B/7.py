def compute_health_points(n, d):
    health_points = 0
    for i in range(n-1):
        for j in range(i+1, n):
            health_points += d[i] * d[j]
    return health_points

if __name__ == '__main__':
    compute_health_points()