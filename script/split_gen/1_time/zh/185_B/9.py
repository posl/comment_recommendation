def solution(n, m, t, a, b):
    battery = n
    time = 0
    for i in range(m):
        battery -= a[i] - time
        if battery <= 0:
            return False
        battery += b[i] - a[i]
        if battery > n:
            battery = n
        time = b[i]
    battery -= t - time
    if battery <= 0:
        return False
    return True
