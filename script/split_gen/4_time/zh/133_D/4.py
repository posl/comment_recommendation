def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (a[i]//2)*2
    for i in range(n):
        if b[i] == 0:
            if i == 0:
                b[n-1] += a[i]//2
                b[i+1] += a[i]//2
            elif i == n-1:
                b[i-1] += a[i]//2
                b[0] += a[i]//2
            else:
                b[i-1] += a[i]//2
                b[i+1] += a[i]//2
    return b
