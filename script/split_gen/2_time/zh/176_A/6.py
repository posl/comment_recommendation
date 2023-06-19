def prob_176_a(n, x, t):
    if n % x == 0:
        return n // x * t
    else:
        return (n // x + 1) * t
