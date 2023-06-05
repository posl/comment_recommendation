def min_distance(k, n, a):
    distance = 0
    for i in range(n-1):
        distance += min(abs(a[i+1]-a[i]), k-abs(a[i+1]-a[i]))
    return distance
