def get_max_comfort(n, a):
    a = [0] + a + [0]
    max_comfort = 0
    for i in range(1, n + 1):
        max_comfort += min(a[i], a[i + 1])
    return max_comfort
