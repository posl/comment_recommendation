def solve(n, a):
    count = 0
    while True:
        i = 0
        for j in a:
            if j % 2 == 0:
                i += 1
        if i == n:
            count += 1
            for j in range(n):
                a[j] = a[j] // 2
        else:
            break
    while True:
        i = 0
        for j in a:
            if j % 3 == 0:
                i += 1
        if i == n:
            count += 1
            for j in range(n):
                a[j] = a[j] // 3
        else:
            break
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            return -1
    return count
