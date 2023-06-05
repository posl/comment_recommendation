def maxComfort(n, a):
    a.append(a[0])
    a.append(a[1])
    max_comfort = 0
    comfort = 0
    for i in range(1, n+1):
        comfort += min(a[i-1], a[i+1])
        max_comfort = max(max_comfort, comfort)
        if comfort < 0:
            comfort = 0
    return max_comfort
