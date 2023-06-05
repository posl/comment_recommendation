def solve(n, b):
    a = [0] * n
    for i in range(n-1):
        if b[i] > b[i+1]:
            a[i+1] = b[i+1]
        else:
            a[i+1] = b[i]
    return sum(a)
