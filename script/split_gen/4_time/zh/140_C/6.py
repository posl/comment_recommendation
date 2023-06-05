def solve(n, b):
    a = []
    a.append(b[0])
    for i in range(1, n-1):
        a.append(max(b[i], b[i-1]))
    a.append(b[n-2])
    return sum(a)
