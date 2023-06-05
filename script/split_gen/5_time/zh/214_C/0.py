def process(n, s, t):
    times = [0] * n
    for i in range(n):
        times[i] = t[i]
        if i == 0:
            times[i] = max(times[i], s[i])
        else:
            times[i] = max(times[i], times[i - 1] + s[i])
    return times
