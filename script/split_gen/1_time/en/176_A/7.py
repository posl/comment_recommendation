def takoyaki(n, x, t):
    return (n // x + 1) * t if n % x else n // x * t
