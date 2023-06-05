def is_possible(N, X, a, b):
    x = 0
    for i in range(N):
        if x + a[i] <= X:
            x += b[i]
        else:
            x += a[i]
        if x == X:
            return True
    return False
