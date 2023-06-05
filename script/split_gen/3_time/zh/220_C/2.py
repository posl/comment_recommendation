def problem220_c(n, a, x):
    b = a * 100
    sum = 0
    for i in range(len(b)):
        sum += b[i]
        if sum > x:
            return i + 1
